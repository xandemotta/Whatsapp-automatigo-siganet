from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def send_whatsapp_message(contact_name, message):
    # Configurar o WebDriver do Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Acessar o WhatsApp Web
    driver.get('https://web.whatsapp.com')
    
    # Esperar um tempo para o usuário escanear o código QR
    print("Escaneie o código QR do WhatsApp")
    time.sleep(20)
    
    # Procurar pelo contato na barra de pesquisa
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.ENTER)
    
    # Esperar um momento para o contato ser carregado
    time.sleep(5)
    
    # Encontrar a caixa de texto para a mensagem
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    
    # Fechar o navegador
    time.sleep(5)
    driver.quit()

# Exemplo de uso
contact_name = "Oi"
message = "Olá, esta é uma mensagem automatizada."
send_whatsapp_message(contact_name, message)
