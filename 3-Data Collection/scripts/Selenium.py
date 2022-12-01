# importement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

def get_driver() : 
    # values 
    link = "https://www.jumia.ma/"



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
    search_bar = driver.find_element(By.ID, "fi-q")
    search_bar.send_keys("Voiture")
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)

    


    time.sleep(500)



get_driver()