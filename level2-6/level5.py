from selenium import webdriver
import os
from time import sleep

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('locator.html')
dr.get(file_path)

# Task 5.1 Click the baidu link a new window will popup, locate the window and enter easonhan.info in the search textfield
dr.find_element_by_link_text('Baidu').click()
old_handle = dr.current_window_handle
for handle in dr.window_handles:
	if old_handle != handle:
		new_handle = handle
		break
dr.switch_to_window(new_handle)
i=dr.find_element_by_id('kw1')
i.click()
i.send_keys('easonhan.info')
dr.find_element_by_id('su1').click()

# Task 5.2 Try to get the href of baidu link and get the url in the same window. Then enter easonhan.info in the search textfield
url=dr.find_element_by_link_text('Baidu').get_attribute('href')
dr.get(url)
i=dr.find_element_by_id('kw1')
i.click()
i.send_keys('easonhan.info')
dr.find_element_by_id('su1').click()