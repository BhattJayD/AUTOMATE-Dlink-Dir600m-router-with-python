from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
	driver = webdriver.Chrome()
	driver.get("http://192.168.0.1/login.htm")
	#time.sleep(5)

	passwd=driver.find_element_by_xpath('//*[@id="password"]')
	#whatpass=input("enter password:- ")
	#time.sleep(5)
	passwd.send_keys('onepiece')
	login=driver.find_element_by_xpath('//*[@id="loginBtn"]')
	login.click()

	time.sleep(1)
	driver.get('http://192.168.0.1/reboot.htm')
	#rebootbtn=driver.find_element_by_xpath('/html/body/blockquote/div/table/tbody/tr/td/table[6]/tbody/tr/td[2]/table/tbody/tr/td/div/form/table/tbody/tr[2]/td/input[1]')
	time.sleep(1)
	rebootbtn=driver.find_element_by_xpath('/html/body/blockquote/div/table/tbody/tr/td/table[6]/tbody/tr/td[2]/table/tbody/tr/td/div/form/table/tbody/tr[2]/td/input[1]')
	rebootbtn.click()
	time.sleep(5)

	driver.close()
except:
	print('got some errors')
	driver.close()