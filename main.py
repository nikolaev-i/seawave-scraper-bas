from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from vars import PATH, site, test_data
from bs4 import BeautifulSoup as bs
from datetime import datetime, tzinfo
from dateutil import tz
import pytz
import sys


def main():
  args = sys.argv[1]

  match args:
    case "test":
      page_source = test_data
      print("using test data")

    case _:
      options = Options()
      options.add_experimental_option("detach", True)
      service = Service(PATH)
      driver = webdriver.Chrome(service=service,
                              options=options)
      driver.get(site)
      dropdownbox = driver.find_elements(by=By.TAG_NAME, value="Option")
      dropdownbox[1].click()                                   
      page_source = driver.page_source
      driver.close()

  
  source = bs(page_source,"html.parser")
  table_header = source.find_all('tbody')[2]
  data_table = table_header.find_all('td')
  data_list = [] 
  single_record = []
  for data in data_table:
    values = data.text.strip('\xa0')
    data_list.append(values)
  for data in data_list:
    if len(single_record) != 8:
      single_record.append(data)
  single_record.extend(single_record[7].split(' '))
  single_record.pop(7)
  print(single_record)




main()






