import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

BCCIHomePage = r'https://www.bcci.tv/international/results'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(BCCIHomePage)
while True:
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                        r'/html/body/div[4]/div/div/div['
                                                                        r'2]/section/button')))
        elementToClick = driver.find_element_by_xpath(r'/html/body/div[4]/div/div/div[2]/section/button')
        elementToClick.click()
        print("Element Clicked")
        time.sleep(3)
    except:
        print("No More pages left")
        break
while True:
    driver.find_element_by_xpath(r'/html/body/div[4]/div/div/div[2]/div/button').click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 600);")
file = open('DS.html', 'w')
file.write(driver.page_source)
file.close()

driver.close()
