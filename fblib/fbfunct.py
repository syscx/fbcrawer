def facebook_login(driver,user,password):
    driver.get('https://www.facebook.com')
    driver.find_element_by_id("email").send_keys(user)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("loginbutton").click()