from selenium import webdriver

driver = webdriver.Chrome('D:/Program Files/webdrivers/chromedriver')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the victim: ')
msg = input('Enter the message: ')
count = int(input('Enter how many messages: '))

input('Press anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//div[@class = "_3u328 copyable-text selectable-text"]')

for i in range(count):
	msg_box.send_keys(msg)
	button = driver.find_element_by_xpath('//button[@class = "_3M-N-"]')
	button.click()