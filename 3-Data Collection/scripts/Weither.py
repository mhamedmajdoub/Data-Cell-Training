from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

def get_driver() : 
    # values 
    link = "https://www.accuweather.com/"
    # program
    # components
    # This is just to install the driver manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    driver.get(link)

    search_bar = driver.find_element(By.CLASS_NAME, "search-input")
    search_bar.send_keys("Rabat")
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)
    
    click_link=driver.find_element(By.XPATH , "//a[contains(text(),'Rabat, Rabat-Salé-Kénitra, MA')]")
    click_link.click()
    time.sleep(5)

    temp=driver.find_element(By.CLASS_NAME , "temp")
    temp.click()
    time.sleep(2)

    temperature=driver.find_element(By.CLASS_NAME,"temperature")
    print(temperature.text)
    time.sleep(2)

    time.sleep(500)
    
get_driver()