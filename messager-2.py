import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def send_whatsapp_message(contact_name, message):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get('https://web.whatsapp.com')
    print("Escaneie o código QR do WhatsApp")
    time.sleep(20)
    
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.ENTER)
    
    time.sleep(5)
    
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    
    time.sleep(5)
    driver.quit()

def send_bulk_messages(contacts_csv):
    df = pd.read_csv(contacts_csv)
    for index, row in df.iterrows():
        send_whatsapp_message(row['Name'], "Olá, esta é uma mensagem automatizada.")
        time.sleep(2)

if __name__ == '__main__':
    contacts_csv = '/mnt/data/contacts.csv'
    send_bulk_messages(contacts_csv)
