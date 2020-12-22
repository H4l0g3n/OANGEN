# Uses Selenium ChromeDriver to grab headlines

import csv
import time
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome


driver = Chrome(executable_path="C:/ChromeDriver/chromedriver.exe")
driver.get("https://www.oann.com/category/newsroom/page/2/")
driver.maximize_window()