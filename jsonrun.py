from urllib.request import urlopen
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

#selenium User login
p = getpass.getpass()
driver = webdriver.Chrome()
driver.get('https://www.facebook.com')
driver.find_element_by_id("email").send_keys('s882852@hotmail.com')
driver.find_element_by_id("pass").send_keys(p)
driver.find_element_by_id("loginbutton").click()

#Scan feed
response = urlopen('https://graph.facebook.com/2345436058812466?fields=id,name,feed.limit(60){link}&access_token=EAAIirR6BbH8BAJww1Kd0ANIY1Yplm4nNcgH8fOSNBlQylTZCnRZAGIJVmb2JJNZC3GtOLfXtHuDxSRTVNS7LPgrq45z1axDYwSIuTa9V3jaGZCQqUsPyDn9GjLFiZAv0BWjk5vTUVYBZBYFJqDzo98R6T1xbAGHGKj36ghHSaBPgZDZD')
data = json.load(response)
json_string = json.dumps(data)
datastore = json.loads(json_string)
itemlen = len(datastore["feed"]["data"])
feeds = datastore["feed"]["data"]

print(itemlen)
print(feeds)

#Access feed
for fv2link in feeds:
    driver.implicitly_wait(1)
    print(fv2link['link'])
    driver.execute_script("window.open('"+fv2link['link']+"');")