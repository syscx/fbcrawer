from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

# Global Variables
driver = None

def facebook_login(password):
    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com')
    driver.find_element_by_id("email").send_keys('f93525048@ntu.edu.tw')
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("loginbutton").click()
    
def load_greatGiftTop():
    driver.execute_script("window.open('https://www.kutumdanevar.com/free-great-gift-package-gifts-for-farmville-2/');")
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(4)

def load_targetPage():
    gift_link = driver.find_element_by_xpath("//a[contains(@title, 'great gift package for the')]")
    driver.execute_script("window.open('"+gift_link.get_attribute("href")+"');")
    driver.switch_to.window(driver.window_handles[2])
    driver.implicitly_wait(4)

def parse_getGift():
    greatGifts = driver.find_elements_by_xpath("//a[contains(@href, 'link/')]")
    print("try to get gifts")
    for one_gift in greatGifts:
        driver.execute_script("window.open('"+one_gift.get_attribute("href")+"');")

def main():
    user_password = getpass.getpass()
    facebook_login(user_password)
    #open tab
    #goto top
    load_greatGiftTop()
    #find alt="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" title="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" /
    #goto href
    #Farmville 2 free great gift package for the
    load_targetPage()
    #Scan and get bottle one by one
    parse_getGift()
    #bottle
    load_bottleTop()
    load_bottlePage()
    parse_getBottle()

if __name__ == '__main__':
    main()

def load_bottleTop():
    driver.execute_script("window.open('https://www.kutumdanevar.com/');")
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(4)

#find alt="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" title="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" /
#goto href

def load_bottlePage():
    bottles_link = driver.find_element_by_xpath("//a[contains(@title, 'baby bottles gifts for the')]")
    driver.execute_script("window.open('"+bottles_link.get_attribute("href")+"');")
    driver.switch_to.window(driver.window_handles[2])
    driver.implicitly_wait(4)

def parse_getBottle():
    bottles = driver.find_elements_by_xpath("//a[contains(@href, 'link/')]")
    for one_bottle in bottles:
        driver.execute_script("window.open('"+one_bottle.get_attribute("href")+"');")