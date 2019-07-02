from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import getpass

def load_greatGiftTop(driver):
    driver.execute_script("window.open('https://www.kutumdanevar.com/free-great-gift-package-gifts-for-farmville-2/');")
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(4)

def load_targetPage(driver):
    gift_link = driver.find_element_by_xpath("//a[contains(@title, 'great gift package for the')]")
    driver.execute_script("window.open('"+gift_link.get_attribute("href")+"');")
    driver.switch_to.window(driver.window_handles[2])
    driver.implicitly_wait(4)

def parse_getGift(driver):
    greatGifts = driver.find_elements_by_xpath("//a[contains(@href, 'link/')]")
    print("try to get gifts")
    for one_gift in greatGifts:
        driver.execute_script("window.open('"+one_gift.get_attribute("href")+"');")

def load_bottleTop(driver):
    driver.execute_script("window.open('https://www.kutumdanevar.com/');")
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(4)

#find alt="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" title="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" /
#goto href

def load_bottlePage(driver):
    bottles_link = driver.find_element_by_xpath("//a[contains(@title, 'baby bottles gifts for the')]")
    driver.execute_script("window.open('"+bottles_link.get_attribute("href")+"');")
    driver.switch_to.window(driver.window_handles[2])
    driver.implicitly_wait(4)

def parse_getBottle(driver):
    bottles = driver.find_elements_by_xpath("//a[contains(@href, 'link/')]")
    for one_bottle in bottles:
        driver.execute_script("window.open('"+one_bottle.get_attribute("href")+"');")