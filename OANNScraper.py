# Uses Selenium ChromeDriver to grab headlines

import csv
import time
from getpass import getpass
from time import sleep

import content as content
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

driver = Chrome(executable_path="C:/ChromeDriver/chromedriver.exe")
driver.get("https://www.oann.com/category/newsroom/page/2/")

headline_boxes = driver.find_elements_by_xpath('//*[@id="main-content"]/article[@*]')
headlines = []
x = 0
while x < 9:
    headlines.append(headline_boxes[x].text)
    print(headlines[x])
    x += 1





