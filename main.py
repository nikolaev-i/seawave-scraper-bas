from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from vars import PATH, site
import bs4 as bs 




options = Options()

options.add_experimental_option("detach", True)

service = Service(PATH)

driver = webdriver.Chrome(service=service,
                          options=options)


driver.get(site)

dropdownbox = driver.find_elements(by=By.TAG_NAME, value="Option")
dropdownbox[1].click()                                   



driver.close()