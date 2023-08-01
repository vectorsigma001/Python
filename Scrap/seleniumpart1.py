from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s=Service("C:/Users/ADMIN/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
search.send_keys("facebook")
