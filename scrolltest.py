from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import getpass

def facebook_login(user,password):
    driver.get('https://www.facebook.com')
    driver.find_element_by_id("email").send_keys(user)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("loginbutton").click()

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

p = getpass.getpass()
f = open("demofile2.txt", "a", encoding="utf-8")
driver = webdriver.Chrome(chrome_options=option)
facebook_login('f93525048@ntu.edu.tw',p)

driver.implicitly_wait(10)
driver.get('https://www.facebook.com/tunwei.wang')
scroll = 0
for scroll in range(5):
    scroll = scroll + 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    driver.implicitly_wait(10)

    #log
    html = driver.page_source
    print(html)
    f.write(html)
    f.write("============================================%%"+str(scroll)+"===========================================\n\n\n\n\n")

    # Once the full page is loaded, we can start scraping
    posts = driver.find_elements_by_class_name("userContentWrapper")

    for post in posts:
        zyngas = post.find_elements_by_xpath("//a[contains(@href, 'zynga')]")
        for links in zyngas:
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

f.close()