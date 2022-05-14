import selenium
from selenium import webdriver

PATH ='/Users/jamesjordan/GitHub/twt_web_scraper/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
print(driver.title)
driver.quit()



