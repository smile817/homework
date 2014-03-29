# coding = utf-8
from selenium import webdriver
import os


dr=webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('test.html')

dr.get(file_path)

url=dr.find_element_by_id('123').get_attribute("href")
print url

dr.get(url)
