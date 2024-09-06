import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def initialize_whatsapp():
    # Configurar o WebDriver do Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Acessar o WhatsApp Web
    driver.get('https://web.whatsapp.com')
    
    # Esperar um tempo para o usuário escanear o código QR
    print("Escaneie o código QR do WhatsApp")
    time.sleep(20)
    
    return driver

def send_whatsapp_message(driver, contact_name, message):
    try:
        # Procurar pelo contato na barra de pesquisa
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.clear()  # Limpar a caixa de pesquisa antes de buscar outro contato
        search_box.send_keys(contact_name)
        search_box.send_keys(Keys.ENTER)
        
        # Esperar um momento para o contato ser carregado
        time.sleep(5)
        
        # Encontrar a caixa de texto para a mensagem
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        
        print(f"Mensagem enviada para {contact_name}")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {contact_name}: {str(e)}")

def format_message(contact_name):
    # Criar a mensagem personalizada com o nome completo da coluna "Name"
    return f"Bom dia {contact_name}, essa é uma mensagem automática que sabe seu nome."

def send_bulk_messages(contacts_csv):
    driver = initialize_whatsapp()  # Inicializar o WhatsApp Web e escanear o QR code uma vez
    
    df = pd.read_csv(contacts_csv)
    for index, row in df.iterrows():
        message = format_message(row['Name'])  # Formatar a mensagem com o nome do contato
        send_whatsapp_message(driver, row['Name'], message)
        time.sleep(2)
    
    driver.quit()

if __name__ == '__main__':
    contacts_csv = r'C:\Users\Mota\Documents\GitHub\Assemblyspeech\transcricao-app_version_2\Whatsapp-automatigo-siganet\teste\contatos.csv'
    send_bulk_messages(contacts_csv)
