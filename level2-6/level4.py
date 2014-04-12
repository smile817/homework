
from selenium import webdriver
import os
from time import sleep

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('locator.html')
dr.get(file_path)


cos=dr.find_elements_by_class_name('btn-default')

for i in cos:
	if i.get_attribute('text') == 'Alert Button':
		i.click() 
		sleep(1)
		alert = dr.switch_to_alert()
		alert.accept()
		sleep(1)
	if i.get_attribute('text') == 'Confirm Button':
		i.click()
		sleep(1)
		confirm = dr.switch_to_alert()
		confirm.dismiss()
		sleep(1)

	if i.get_attribute('text') == 'Prompt Button':
		i.click()
		sleep(1)
		prompt=dr.switch_to_alert()
		prompt.send_keys('key')
		sleep(1)
		prompt.accept()

