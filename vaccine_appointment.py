from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from twilio.rest import Client
from time import time, sleep

wd_path="/home/ayyuce/chrome/chromedriver"  #do not forget to change the path
wd = webdriver.Chrome(executable_path=wd_path)

while True:
    
    wd.get("https://enabiz.gov.tr/")
    usrname = wd.find_element_by_id("username")
    usrname.send_keys('ID_number')
    passwd = wd.find_element_by_id("Sifre")
    passwd.send_keys("your_password")
    wd.find_element_by_id("btnGiris").click()

    wd.get("https://enabiz.gov.tr/AsiTakvimi?whichTab=True")

    msg = None
    for elem in wd.find_elements_by_id("dvCovidAsi"):
        msg = elem.text
    print(msg)

    account_sid = "YOUR_ACCOUNT_SID"
    auth_token = "YOUR_AUTH_TOKEN"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body=msg,
                                from_='whatsapp:+14155238886',
                                to='whatsapp:+905555555555' #your phone number

                            )

    print(message.sid)
    sleep(3600)
