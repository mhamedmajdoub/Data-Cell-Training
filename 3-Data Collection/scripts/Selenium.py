# importement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

def get_driver() : 
    # values 
    link = "https://www.avito.ma/"



    # program
    # components
    # This is just to install the driver manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 



    # In order to interact with every element in selenium we must call driver.
    # Here is the new syntaxe of the selenium, dikchi lekher

    # This is to do a research 
    # This last version of selenium doesn't accept class names with spaces

    # Always do researches on the class name so you won't miss a component

    driver.get(link)
    search_bar = driver.find_element(By.CLASS_NAME, "sc-1i9i8oo-0")
    search_bar.send_keys("Voiture")
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)

    # Narrow by a city 
    buttons = driver.find_elements(By.CLASS_NAME, "sc-13f8628-1")
    city = buttons[1]
    city.click()
    time.sleep(2)

    ville = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/div[1]")
    ville.click()
    time.sleep(2)

    search_button = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[3]/button[1]")
    search_button.click()


    time.sleep(500)



get_driver()