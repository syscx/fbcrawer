from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import getpass
import fblib

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.headless = True
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

p = getpass.getpass()
driver = webdriver.Chrome(chrome_options=option)
fblib.facebook_login(driver,'f93525048@ntu.edu.tw',p)
checking_list = ["evening.tkc", "chou.wang.39", "wang.leox"]
i = 0
while i < len(checking_list):
    driver.implicitly_wait(5)
    print('https://www.facebook.com/'+checking_list[i])
    driver.get('https://www.facebook.com/'+checking_list[i])
    i = i + 1
    scroll = 0
    for scroll in range(2):
        scroll = scroll + 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(5)
        posts = driver.find_elements_by_class_name("userContentWrapper")
        for post in posts:
            zyngas = post.find_elements_by_xpath("//a[contains(@href, 'zynga')]")
            for links in zyngas:
                driver.execute_script("window.open('"+links.get_attribute("href")+"');")
                print(links.get_attribute("href"))
            # Creating first CSV row entry with the page name
            analysis = ["feeds"]
            # Creating post text entry
            text = ""
            text_elements = post.find_elements_by_css_selector("p")
            for p in text_elements:
                text += p.text.strip()
                analysis.append(text)
            # Write row to console
            print(analysis)