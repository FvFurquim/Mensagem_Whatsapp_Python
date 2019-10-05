from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import os
import sys
import csv
import threading


driver = webdriver.Chrome('D:/Program Files/webdrivers/chromedriver')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the victim: ')

input('Press anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

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

repeatfun()