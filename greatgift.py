from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
from fblib.fbfunct import facebook_login
from fblib.greatgift import *
    
def main():
    user_password = getpass.getpass()
    global driver
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    facebook_login(driver,'f93525048@ntu.edu.tw',user_password)
    #open tab
    #goto top
    load_greatGiftTop(driver)
    #find alt="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" title="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" /
    #goto href
    #Farmville 2 free great gift package for the
    load_targetPage(driver)
    #Scan and get bottle one by one
    parse_getGift(driver)
    #bottle
    load_bottleTop(driver)
    load_bottlePage(driver)
    parse_getBottle(driver)

if __name__ == '__main__':
    main()