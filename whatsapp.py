from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
wait5 = WebDriverWait(driver, 5)
msg = "This is Test *Message*" #Messgae to be Send
count1=10 #Number of Times
targets =["My Airtel"] # Contacts
i=0
counter=1
time.sleep(30)
while True:
    for target in targets:
        newChat = driver.find_element_by_xpath(
            "/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div").click()
        contact = driver.find_element_by_xpath(
            "/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]")
        contact.send_keys(target)
        time.sleep(10)
        selectContact = driver.find_element_by_class_name("_3vPI2").click()
        time.sleep(10)
        while i <= count1:
            message = driver.find_elements_by_class_name("_13NKt")
            message[1].send_keys(msg, Keys.ENTER)
            i = i + 1

    i=0
    if counter==len(targets):
        break
    counter=counter+1
time.sleep(30)
driver.close()