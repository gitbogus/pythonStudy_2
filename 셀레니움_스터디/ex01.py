from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/sangmin/Desktop/Study List/Study_Collection/chromedriver.exe')

    # Navigate to Url
driver.get("https://www.seleniumeasy.com/")

    # Get all the elements available with tag name 'p'
#elements = driver.find_elements(By.TAG_NAME, 'p')

#for e in elements:
    #print(e.text)