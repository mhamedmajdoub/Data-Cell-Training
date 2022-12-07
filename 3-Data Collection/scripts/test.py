from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

def get_driver() : 
    link = "https://www.avito.ma/"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
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


    #images=driver.find_elements(By.XPATH,"//body/div[@id='__next']/div[1]/main[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div/a[1]/div[1]/div[1]/img[1]")
    #for image in images:
        #print(image.get_attribute("src"))
    #time.sleep(2)
    annonces=driver.find_elements(By.XPATH,"//body/div[@id='__next']/div[1]/main[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div/a[1]")
    links=[]
    for item in annonces:
        links.append(item.get_attribute("href"))
        print(item)
    time.sleep(2)
    '''liste_noms=[]
    liste_prices=[]
    liste_places=[]
    liste_sellers=[]
    liste_dates=[]'''
    file_path = r'C:\Users\hp\Desktop\text.txt'
    file=open(file_path, 'w')
    for i in range(0,5):
        driver.get(links[i])
        nom=driver.find_element(By.XPATH,"//h1[contains(text(),'Dacia sandero stepway Diesel 2013')]")
        print(nom.text())
        file.write(nom.text())
        time.sleep(2)
        prices=driver.find_elements(By.XPATH,"//body/div[@id='__next']/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p[1]")
        file.write(prices[i].text())
        time.sleep(2)
        places=driver.find_elements(By.XPATH,"//span[contains(text(),'Casablanca')]")
        file.write(places[i].text())
        time.sleep(2)
        sellers=driver.find_elements(By.XPATH,"//p[contains(text(),'Fatima')]")
        file.write(sellers[i].text())
        time.sleep(2)
        dates=driver.find_elements(By.XPATH,"//body/div[@id='__next']/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/ol[1]/li[8]/span[2]")

        time.sleep(2)
    file.close()

    '''for i in range(0,len(noms)):
        liste_noms.append(noms[i].text)
    for i in range(0,5):
        liste_prices.append(prices[i].text)
    for i in range(0,5):
        liste_places.append(places[i].text)
    for i in range(0,5):
        liste_sellers.append(sellers[i].text)
    for i in range(0,5):
        liste_dates.append(dates[i].text)
    print(liste_noms)
    print(liste_prices)
    print(liste_places)
    print(liste_sellers)
    print(liste_dates)'''

    time.sleep(500)
get_driver()