from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

def get_driver() : 
    listes_des_noms=["Mhamed majdoub","Abdelmajid Nidnasser"]
    link = "https://www.linkedin.com/home"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    driver.get(link)

    mail = driver.find_element(By.ID, "session_key")
    mail.send_keys("majdoub.mhamed@inemail.ine.inpt.ma")
    time.sleep(2)

    password = driver.find_element(By.ID, "session_password")
    password.send_keys("Majdoub16")
    time.sleep(2)

    connecter = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
    connecter.click()
    time.sleep(5)

    for nom in listes_des_noms:
        search_bar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
        search_bar.send_keys(nom)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)

        #search=driver.find_element(By.ID , "msg-overlay-list-bubble-search__search-typeahead-input")
        #search.send_keys(nom)
        #time.sleep(2)

        chose=driver.find_element(By.XPATH,"//body/div[5]/div[3]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/a[1]/span[1]/span[1]")
        chose.click()
        time.sleep(2)

        more=driver.find_element(By.CLASS_NAME,"mercado-match")
        more.click()
        time.sleep(2)

        connecter=driver.find_element(By.XPATH,"//body/div[5]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[4]/div[1]/span[1]")
        connecter.click()
        time.sleep(2)



        add_note=driver.find_element(By.CLASS_NAME,"artdeco-button__text")
        add_note.click
        time.sleep(2)

        type_note=driver.find_element(By.ID,"custom-message")
        type_note.send_keys("kalam fa7ich. Cordialement!")
        type_note.send_keys(Keys.ENTER)
        time.sleep(2)

        send_note=driver.find_element(By.CLASS_NAME,"artdeco-button__text")
        send_note.click
        time.sleep(2)

    time.sleep(500)

get_driver()