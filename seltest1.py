from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
# driver.get('https://www.facebook.com')
driver.get("http://www.google.com/")
# driver.find_element_by_id("email").send_keys('s882852@gmail.com')
# driver.find_element_by_id("pass").send_keys('xx')
# driver.find_element_by_id("loginbutton").click()
#open tab
#goto top page / Gifx

#https://www.kutumdanevar.com/
# driver.execute_script("window.open('https://www.kutumdanevar.com/');")

driver.execute_script("window.open('http://ranking.rakuten.co.jp/daily/100533/');")
driver.switch_to.window(driver.window_handles[1])

#find alt="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" title="Farmville 2 free 20 baby bottles gifts for the 1st time in 07 June 2019 Friday" /
#goto href
# bottles_link = driver.find_element_by_xpath("//a[contains(@alt, 'baby bottles gifts for the')]")
# driver.execute_script("window.open('"+bottles_link.get_attribute("href")+"');")

#search src="images/farmville-2-free-20-baby-bottles.png
#goto href by open new link
#goto href="link/138760/gunluk/farmville-2-free-20-baby-bottles-gifts-for-the-1st-time-in-07-june-2019-friday/"
# bottles = driver.find_elements_by_xpath("//a[contains(@src, 'farmville-2-free-20-baby-bottles.png')]")
# for one_bottle in bottles:
#   driver.execute_script("window.open('"+one_bottle.get_attribute("href")+"');")

# Make the tests...
# Scan
# elements = driver.find_element_by_xpath("//link[@href='/daily/100533/p=2/'  ]")
driver.implicitly_wait(2)
#//*[contains(text(), 'Best Choice')]
elements = driver.find_elements_by_xpath("//a[contains(@href, 'item.rakuten.co.jp')]")

# https://item.rakuten.co.jp/
# Enter link
print(elements);
for item in elements:
    driver.execute_script("window.open('"+item.get_attribute("href")+"');")


