import os
from selenium import webdriver

# os.environ['PATH'] += r"C:/Users/sangmin/Desktop/Study List/git_practice/"
driver = webdriver.Chrome('C:/Users/sangmin/Desktop/Study List/git_practice/chromedriver.exe')
driver.get("https://www.seleniumeasy.com/")
driver.implicitly_wait(3)
menu = driver.find_element(By.ID,"<h2>Selenium Python</h2>")


menu.click()

