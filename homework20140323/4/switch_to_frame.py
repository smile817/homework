# coding = utf-8
from selenium import webdriver
import os


dr=webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('test.html')

dr.get(file_path)
frames=dr.find_elements_by_tag_name("frame")
dr.switch_to_frame(frames[2])



