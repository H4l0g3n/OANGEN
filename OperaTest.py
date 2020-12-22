from selenium import webdriver
from time import sleep
Driver =  webdriver.Opera(executable_path="C:\OperaDriver\operadriver_win64/operadriver.exe")

# The profile where I enabled the VPN previously using the GUI.
opera_profile = '/home/dan/.config/opera'
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=' + opera_profile)
driver = webdriver.Opera(options=options)
driver.get('https://whatismyipaddress.com')
sleep(10)
driver.quit()