from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import getpass
import csv
import time 
import fblib

def load_bottleTop(driver):
    driver.implicitly_wait(2)
    driver.execute_script("window.open('https://www.kutumdanevar.com/');")
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(4)

def parse_getBottle(driver):
    bottles_link = driver.find_element_by_xpath("//a[contains(@title, 'baby bottles gifts for the')]")
    driver.execute_script("window.open('"+bottles_link.get_attribute("href")+"');")
    driver.switch_to.window(driver.window_handles[2])
    driver.implicitly_wait(2)

#find alt="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" title="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" /
#goto href
def get_bottles(driver):
    #Scan and get bottle one by one
    bottles = driver.find_elements_by_xpath("//a[contains(@href, 'link/')]")
    print("try to get bottles")

    print(bottles)
    for one_bottle in bottles:
        driver.execute_script("window.open('"+one_bottle.get_attribute("href")+"');")