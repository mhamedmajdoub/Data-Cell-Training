from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pandas as pd

def get_driver() :
    informations={"job": [],"type_offre":[],"domaine":[],"city":[],"description":[]}
    link = "http://www.stage.ma/"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    driver.get(link)
    time.sleep(2)
    offres=driver.find_element(By.CLASS_NAME,"btn-vis3")
    offres.click()
    time.sleep(2)

    offre=driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[1]/a[1]")
    offre.click()
    time.sleep(2)

    job=driver.find_element(By.XPATH,"//h3[contains(text(),'Recrutement massif (opérateur de saisie | Telecons')]")
    print(job.text)
    informations["job"].append(job.text)
    time.sleep(2)

    type_offre=driver.find_element(By.XPATH,"//label[contains(text(),'Pré-embauche')]")
    print(type_offre.text)
    informations["type_offre"].append(type_offre.text)
    time.sleep(2)

    domaine=driver.find_element(By.XPATH,"//label[contains(text(),'Marketing/ Communication/ Publicité')]")
    print(domaine.text)
    informations["domaine"].append(domaine.text)
    time.sleep(2)

    city=driver.find_element(By.XPATH,"//strong[contains(text(),'Fès')]")
    print(city.text)
    informations["city"].append(city.text)
    time.sleep(2)

    description=driver.find_element(By.XPATH,"//body/div[@id='detail_offre']/div[1]/div[4]/div[1]/div[1]/p[1]")
    print(description.text)
    informations["description"].append(description.text)
    time.sleep(2)

    df=pd.DataFrame(informations)
    
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter("stage.xlsx", engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='stage', index=False)

# Close the Pandas Excel writer and output the Excel file.
    writer.close()

    time.sleep(500)

get_driver()
