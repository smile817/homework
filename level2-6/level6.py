from selenium import webdriver
import os
from time import sleep

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('locator.html')
dr.get(file_path)


#Task 6.1 Type something in the outsize textfield

dr.find_element_by_name('outsize').send_keys('something')

# Task 6.2 Type something in the inside textfield
inside = dr.find_element_by_tag_name('iframe')
dr.switch_to_frame(inside)
dr.find_element_by_name('inside').send_keys('something')









#Task 6.2 Type something in the inside textfield