# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH ='/Users/jamesjordan/GitHub/twt_web_scraper/chromedriver'

driver = webdriver.Chrome(PATH)


driver.get('https://orteil.dashnet.org/cookieclicker/')
actions = ActionChains(driver)
actions.click()
actions.perform()


link = driver.find_element_by_link_text('Python Programming')
link.click()

try: 
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.clear()
    element.click()

    driver.back()
    driver.forward()

except: 
    driver.quit()