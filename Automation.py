from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from getpass import getpass

username = input('\nWhat is your username? - ')
password = getpass('\nWhat is your password? - ')
print("\nDon't worry no usernames or passwords are saved in this programme!")
receiver = input('\nWho do you want to message today? (Please try and type the exact username of the reciever) - ')
message = input('\nWhat message do you want to send? - ')
print('\n')

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')
time.sleep(1)
instagram_login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
instagram_password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
instagram_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')

instagram_login.send_keys(username)
instagram_password.send_keys(password)
instagram_button.click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(2)
instagram_dm = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
instagram_dm.click()
time.sleep(2)
search_person = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button')
search_person.click()
time.sleep(1)
instagram_search_dm = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input')
instagram_search_dm.send_keys(receiver)
time.sleep(3)
instagram_dm_to = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button/span')
instagram_dm_to.click()
time.sleep(2)
instagram_next = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button')
instagram_next.click()
time.sleep(3)
instagram_msg = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
instagram_msg.send_keys(message)
time.sleep(1)
instagram_msg.send_keys(u'\ue007')

msg_by_person = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[30]/div[2]/div/div/div/div/div/div/div')
instagram_msg.send_keys('I am mad at you')
time.sleep(1)
instagram_msg.send_keys(u'\ue007')
os.system('clear')
print(q)
exit()






