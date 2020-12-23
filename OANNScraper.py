# Uses Selenium ChromeDriver to grab headlines

import csv
import time
from getpass import getpass
from time import sleep

# import content as content
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, InvalidSessionIdException
from selenium.webdriver import Chrome

driver = Chrome(executable_path="C:/ChromeDriver/chromedriver.exe")
driver.get("https://www.oann.com/category/newsroom/page/2/")
newsroom_page_count = 2
newsroom_page_max = driver.find_element_by_xpath('//*[@id="main-content"]/div/a[5]').text
int(newsroom_page_max)


def extract_article_info(article_object):
    headline = article_object.find_element_by_xpath('.//header/h3/a')
    article_description = article_object.find_element_by_xpath('.//div[2]/p')
    article_info = (headline.text, article_description.text)
    return article_info


data = []
article_objects = driver.find_elements_by_xpath('//*[@id="main-content"]/article[@*]')
for article_object in article_objects:
    article_info = extract_article_info(article_object)
    print(article_info)
    data.append(article_info)

while driver.find_element_by_xpath('//*[@id="main-content"]'):
    article_objects = driver.find_elements_by_xpath('//*[@id="main-content"]/article[@*]')
    for article_object in article_objects:
        article_info = extract_article_info(article_object)
        print(article_info)
        data.append(article_info)
        try:
            next = driver.find_element_by_xpath('//*[@class="next page-numbers"]')
            if next.is_displayed():
                next.click()
                newsroom_page_count += 1
                print(newsroom_page_count)
        except StaleElementReferenceException:
            print(55 * "-")
            driver.close()
            #print(55 * "-")
            #driver.close()
