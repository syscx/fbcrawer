from urllib.request import urlopen
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import getpass
import csv
import time
import sys

def facebook_login(user,password):
    driver.get('https://www.facebook.com')
    driver.find_element_by_id("email").send_keys(user)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("loginbutton").click()

def scan_feed():
#Scan feed
    response = urlopen('https://graph.facebook.com/2345436058812466?fields=id,name,feed.limit(40){link}&access_token=EAAIirR6BbH8BAJww1Kd0ANIY1Yplm4nNcgH8fOSNBlQylTZCnRZAGIJVmb2JJNZC3GtOLfXtHuDxSRTVNS7LPgrq45z1axDYwSIuTa9V3jaGZCQqUsPyDn9GjLFiZAv0BWjk5vTUVYBZBYFJqDzo98R6T1xbAGHGKj36ghHSaBPgZDZD')
    data = json.load(response)    
    json_string = json.dumps(data)
    datastore = json.loads(json_string)
    feeds = datastore["feed"]["data"]
    return feeds

def access_feed(feeds):
    #Access feed
    count = 0
    for fv2link in feeds:
        count=count + 1
        driver.implicitly_wait(1)
        driver.execute_script("window.open('"+fv2link['link']+"');")
        #debug mode
        #driver.switch_to.window(driver.window_handles[count])#0+fb magic number
        #driver.implicitly_wait(3)
        #print("capture"+str(count)+".png")
        #driver.get_screenshot_as_file("capture"+str(count)+".png")

def main():
    global driver
    path = 'testfileread.txt'
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            #driver = webdriver.Chrome()
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(options=options)
            facebook_login(row[0],row[1])
            feeds = scan_feed()
            access_feed(feeds)
            time.sleep(100)
            driver.quit()

if __name__ == '__main__':
    main()