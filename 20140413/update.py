# coding:utf-8
import unittest
from selenium import webdriver
import os
import time

class Update_Select(unittest.TestCase):
	domain = ''
	dr = None
	def setUp(self):
		self.domain = os.getenv('TEST_ENV','http://localhost/')
		self.dr = webdriver.Chrome()
		print 'Start test!'

	# def test_select(self):
	# 	obstr = 'title for 1397376880.44'
	# 	#登录
	# 	user_name = 'admin'
	# 	password =  'admin123'
	# 	self.login(user_name, password)
	# 	#进入首页
	# 	self.dr.get(self.domain + 'wordpress')
	# 	#查找目标title
	# 	self.select(obstr)
			

	def test_update(self):
		#登录
		user_name = 'admin'
		password =  'admin123'
		self.login(user_name, password)
		#进入id=‘post-24’的文章修改页面
		post_id='24'
		self.dr.get(self.domain + 'wordpress/wp-admin/post.php?post=' + post_id +'&action=edit')
		time.sleep(2)
		#修改title和content
		update_title = 'update title %s' %(time.time())
		update_content = 'update content %s' %(time.time())
		self.dr.find_element_by_name('post_title').clear()
		self.dr.find_element_by_name('post_title').send_keys(update_title)
		self.set_content(update_content)
		self.dr.find_element_by_id('publish').click()

		# 进入站点首页
		self.dr.get(self.domain + 'wordpress/')

		# 查找目标文档
		self.select(update_title)



	def select(self,obstr):
		title = self.dr.find_elements_by_class_name('entry-title')
		txt = []
		for i in range(0,len(title)-1):
			txt = txt + [title[i].text]
		if obstr in txt:
			print '%s is in page' %(obstr)
		else :
			print '%s is not in page' %(obstr)

	def login(self,user_name,password):
		self.dr.get(self.domain + 'wordpress/wp-login.php')
		self.dr.find_element_by_id('user_login').send_keys(user_name)
		self.dr.find_element_by_id('user_pass').send_keys(password)
		self.dr.find_element_by_id('wp-submit').click()

	def set_content(self, content):
		set_wyswyg_js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML="%s"' %(content)
		self.dr.execute_script(set_wyswyg_js)


	def tearDown(self):
		self.dr.quit()
		print 'End test!'



if __name__ == '__main__':
	unittest.main()
