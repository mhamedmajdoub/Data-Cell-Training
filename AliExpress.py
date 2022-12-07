from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pandas as pd

def get_driver() :
    informations={"job": [],"type_offre":[],"domaine":[],"city":[],"description":[]}
    link = "https://www.aliexpress.com/"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    driver.get(link)
    time.sleep(2)
    search_bar= driver.find_element(By.XPATH,"//input[@id='search-key']")
    search_bar.send_keys("football")
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)

    elements=driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[2]/div[5]/a[1]/div[1]/img[1]")
    elements.click()
    time.sleep(2)

    
        
    
    time.sleep(500)

get_driver()