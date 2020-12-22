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

def get_headline_data(box):
    try:
        headline_text = box.find_element_by_xpath('//*[@id="main-content"]/article[]/header/h3/a/text()').text
        print(headline_text)
        return(headline_text)
    except NoSuchElementException:
        return

headline_boxes = driver.find_elements_by_xpath('//*[@id="main-content"]/article')

for box in headline_boxes:
    headline = get_headline_data(box)
    print(headline)
