from measurments import Measurment
from selenium import webdriver
from base import Session, engine, Base
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from vars import PATH, site, test_data
from bs4 import BeautifulSoup as bs
from datetime import datetime, tzinfo, timedelta
from dateutil import tz
import pytz
import sys


#def selenium_run():

#def scrape(location):



def main():

  Base.metadata.create_all(engine)

  session = Session()
  args = sys.argv[1]

  match args:
    case "test":
      page_source = test_data
      print("using test data")

    case "real":
      options = Options()
      options.add_experimental_option("detach", True)
      service = Service(PATH)
      driver = webdriver.Chrome(service=service,
                              options=options)
      driver.get(site)

      date_input = driver.find_element(By.ID,value="TextBox1")
      current_date_str = date_input.get_attribute("value")
      current_date = datetime.strptime(current_date_str, "%Y/%m/%d %H:%M:%S")
      one_year_ago = current_date - timedelta(days=1)
      driver.execute_script(f"arguments[0].value = '{one_year_ago.strftime('%Y/%m/%d %H:%M:%S')}';", date_input)
      driver.execute_script("__doPostBack('TextBox1','');")
      dropdownbox = driver.find_elements(By.TAG_NAME, value="Option")
      driver.implicitly_wait(15)
      dropdownbox[1].click()     
      driver.implicitly_wait(15)                              
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
        if len(single_record) == 8:
          single_record.extend(single_record[7].split(' '))
          single_record.pop(7)
          date_obj = datetime.strptime(single_record[7], "%d.%m.%Y")
          single_record[7] = date_obj.strftime("%Y-%m-%d")
          single_record[3] = int(single_record[3].split(".")[0])
          if '' == single_record[6]:
            single_record[6] = 0
          measurment = Measurment(single_record[0],single_record[7],single_record[8],single_record[1],single_record[2],single_record[3],single_record[4],single_record[5],single_record[6])
          session.add(measurment)
          single_record = []
          session.commit()
          session.close






main()






