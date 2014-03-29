from selenium import webdriver
import os
import random

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('checkboxradio.html')
dr.get(file_path)



def random_select(what,count):
	list=[1,2,3,4,5,6]
	m=random.sample(list,count)
	for n in m:
		num=str(n)
		dr.find_element_by_name(what+num).click() 

random_select('checkbox',3)
random_select('radio',1)
