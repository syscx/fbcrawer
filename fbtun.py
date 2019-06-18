from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

p = getpass.getpass()
driver = webdriver.Chrome()
driver.get('https://www.facebook.com')
driver.find_element_by_id("email").send_keys('f93525048@ntu.edu.tw')
driver.find_element_by_id("pass").send_keys(p)
driver.find_element_by_id("loginbutton").click()
#open tab
#goto top
driver.implicitly_wait(2)
#Tun Profile
#driver.execute_script("window.open('https://www.kutumdanevar.com/');")
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(5)
#find alt="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" title="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" /
#goto href

bottles_link = driver.find_element_by_xpath("//a[contains(@title, 'baby bottles gifts for the')]")
driver.execute_script("window.open('"+bottles_link.get_attribute("href")+"');")
driver.switch_to.window(driver.window_handles[2])
driver.implicitly_wait(2)

#Scan and get bottle one by one
bottles = driver.find_elements_by_xpath("//a[contains(@href, 'link/')]")
print("try to get bottles")

print(bottles)
for one_bottle in bottles:
    driver.execute_script("window.open('"+one_bottle.get_attribute("href")+"');")