from selenium import webdriver
import time
import os
import random

dr = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('locator.html')
dr.get(file_path)

# task2.1 Select all the checkboxes
checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')
for i in checkboxes:
	i.click()

# task 2.2 Select frist two checkboxes
checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')
for i in [0,1]:
	checkboxes[i].click()

# task 2.3 Select last two checkboxes
checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')
for i in [-1,-2]:
	checkboxes[i].click()

# task 2.4 Random select one checkbox
checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')
i=random.randint(0,3)
checkboxes[i].click()


# task 2.5 Random select two checkbox
checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')
list=[0,1,2,3]
i=random.sample(list,2)
for j in i:
	checkboxes[j].click()

# task 2.6 Toggle select checkbox. if the checkbox is selected, unselect it, else select it.
checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')
for i in checkboxes:
	i.click()

# task 2.7  Define a method which accept 1 parameters(count). This method will random select checkboxes with quantity of count.
def random_select(count):
	checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')
	list=[0,1,2,3]
	i=random.sample(list,count)
	for j in i:
		checkboxes[j].click()
random_select(3)

# task 2.8 Select radio by value.
radios=dr.find_elements_by_css_selector('input[type=radio]')
for i in radios:
	if i.get_attribute('value')=='third':
		i.click()





# task 2.9 Random select one radio
radios=dr.find_elements_by_css_selector('input[type=radio]')
i=random.randint(0,3)
radios[i].click()





# task 2.10 define a method which accept 2 parameters(type, count).

def select(type,count):
	if type=='checkbox':
		checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')
		list=[0,1,2,3]
		for i in random.sample(list,count):
			checkboxes[i].click()
	if type == 'radio':
		radios=dr.find_elements_by_css_selector('input[type=radio]')
		i=random.randint(0,3)
		radios[i].click()


select('checkbox',2)

select('radio',3)