import time
from selenium.common.exceptions import (
    TimeoutException, WebDriverException
)

def facebook_login(driver,user,password):
    i = 0
    while i < 6:
        try:
            driver.get('https://www.facebook.com')
            driver.find_element_by_id("email").send_keys(user)
            driver.find_element_by_id("pass").send_keys(password)
            time.sleep(1)
            driver.find_element_by_id("loginbutton").click()
            time.sleep(3)
        except TimeoutException:
            i = i + 1
            print("Timeout, Retrying... (%(i)s/%(max)s)" % {'i': i, 'max': 5})
            continue
        else:
            return True