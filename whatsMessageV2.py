from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'C:/Users/Andre/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

input('Press anything after scanning QR code')
while 1 == 1:
	try:
		name = input('Escreva os nomes dos chats separados por virgura: ')
		names = name.split(", ")
		namesLen = len(names)
		msg = input('Escreva a mensagen: ')
		count = int(input('Digite o numero de mensagens: '))
		tempo = int(input('Digite, em segundos, o tempo de delay entre as mensagens: '))

		for x in range(namesLen):

			user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(names[x]))
			user.click()

			msg_box = driver.find_element_by_xpath('//div[@class = "_1Plpp"]') #Classe da div que escreve as mensagens
			print("Enviando mensagem para "+ names[x])
			for i in range(count):
				msg_box.send_keys(msg)
				button = driver.find_element_by_xpath('//button[@class = "_35EW6"]') #Classe do botão que envia a mensagem
				button.click()
				print(i+1," mensagens enviadas")
				time.sleep(tempo)
		if input("Enviar mais mensagens? (s/n) ") == "n":
			break
	except Exception as e:
		print("Eita deu ruim:")
		print(e)
