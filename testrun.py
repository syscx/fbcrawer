from urllib.request import urlopen
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import csv
import time 

def facebook_login(user,password):
    global driver
    driver = webdriver.Chrome()
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

def access_feed():
    driver.execute_script("window.open('https://www.google.com');")

def main():
    global driver
    #driver = webdriver.Chrome()
    path = 'testfileread.txt'
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            driver = webdriver.Chrome()
            #facebook_login(row[0],row[1])
            #feeds = scan_feed()
            access_feed()
            access_feed()
            time.sleep(3)
            driver.quit()

def readpass():
    path = 'testfileread.txt'
    with open(path, "r") as file:
        for line in file:
            print(line)

if __name__ == '__main__':
    main()