# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:31:06 2017

@author: Khan
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from requests import get
from bs4 import BeautifulSoup as bs
import keyboard
import time
import click
import os
import sys
import csv
import threading


chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + os.path.dirname(sys.argv[0]))
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()

driver.get("https://goo.gl/WCS3hC")
time.sleep(25)

target = 'Bacanos'

panel = driver.find_element_by_class_name('chatlist-panel-body')

elem = None
a = 0
while elem is None:
    a += 300
    try:
        driver.execute_script('arguments[0].scrollTop = %s' %a, panel)
        elem = driver.find_element_by_xpath('//span[@title=' + target + ']')
    except:
         pass

ac = ActionChains(driver)
ac.move_to_element(elem).click().perform()
time.sleep(2)

url = driver.page_source

def repeatfun():
    threading.Timer(5.0, repeatfun).start()
    url = driver.page_source
    soup = bs(url, "lxml")

    try:
        gotdiv = soup.find_all("div", { "class" : "msg msg-group" })[-1]
    except IndexError:
        gotdiv = 'null'

    if gotdiv == 'null':
        div = soup.find_all("div", { "class" : "bubble bubble-text copyable-text" })[-1]
        #print(div)
    else:
        div = soup.find_all("div", { "class" : "msg msg-group" })[-1]

    text = div.find_all('span')
    print(text)
    
    try:
        gottext = text[4].find_all(text=True)[1]
    except IndexError:
        gottext = 'null'

    if gottext == 'null': 
        div = soup.find_all("div", { "class" : "chat-title" })[-1]
        name = div.find_all(text=True)[1]
        try:
            msg = text[-2].find_all(text=True)[1].lower()
        except IndexError:
            msg = "You replied last"
        time = text[-1].find(text=True)

    else: #group
        name = text[3].find_all(text=True)[1]
        try:
            msg = text[4].find_all(text=True)[1].lower()
        except IndexError:
            msg = "You replied last"
        try:
            time = text[-2].find(text=True)
        except:
            time = "None"          
        

    print(name, msg, time)
    
    try:
        prevmsg = prevmsg
    except:
        prevmsg = "first"

    try:
        prevtime = prevtime
    except:
        prevtime = "first"

    if msg == "You replied last":
        prevmsg = msg
        prevtime = time
        print(msg)

    elif prevmsg != msg and prevtime != time:
    
        if "buddy" in msg:

         with open('dict.csv', "r") as f:
            reader = csv.reader(f)
            chat = {}

            for row in reader:
                key = row[0]
                chat[key] = row[1:]
         try:
            gotreply = chat[msg]
         except KeyError:
            gotreply = 'null'

         print(gotreply)

         if gotreply == 'null':
            string = "Sorry! I didn't understand. I'm still learning."
            input_box = driver.find_element_by_class_name('pluggable-input-body')
            input_box.send_keys(string)
            driver.find_element_by_xpath('//span[@data-icon="send"]').click()
         else:
            input_box = driver.find_element_by_class_name('pluggable-input-body')
            input_box.send_keys(gotreply)
            driver.find_element_by_xpath('//span[@data-icon="send"]').click()


        else:
            print("The message is not for you")

        prevmsg = msg
        prevtime = time

    else:
        prevmsg = msg
        prevtime = time
        print("It's an old message")

repeatfun()


#driver.close()

