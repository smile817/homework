from selenium import webdriver
import os
import random

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('locator.html')
dr.get(file_path)

# task 3.1 Select an option by value
dropdown=dr.find_element_by_name('user')
dropdown.click()
values=dropdown.find_elements_by_tag_name('option')
for i in values:
	if i.get_attribute('value')=='2':
		i.click()


task 3.2 Select an option by text

dropdown=dr.find_element_by_name('user')
dropdown.click()
texts = dropdown.find_elements_by_tag_name('option')
for i in texts:
	if i.get_attribute('text') == 'jack':
		i.click()

# task 3.3 Define a method that random select an option and return its text
def random_select():
	dropdown=dr.find_element_by_name('user')
	dropdown.click()
	texts = dropdown.find_elements_by_tag_name('option')
	i=random.randint(0,3)
	texts[i].click()
	print texts[i].get_attribute('text')
	return texts[i].get_attribute('text')

random_select()

