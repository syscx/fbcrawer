from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import getpass
import csv
import time 
import fblib
from fblib.fbfunct import facebook_login
from fblib.bottlelib import *

def main():
    p = getpass.getpass()
    global driver
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    facebook_login(driver,'f93525048@ntu.edu.tw',p)
    load_bottleTop(driver)
    parse_getBottle(driver)
    get_bottles(driver)
    time.sleep(100)
    driver.quit()

if __name__ == '__main__':
    main()