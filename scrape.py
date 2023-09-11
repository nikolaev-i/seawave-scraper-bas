from bs4 import BeautifulSoup as bs
import requests


site = "http://sea.meteo-varna.net/"
r = requests.get(site)
status = r.status_code
source = r.content
parse = bs(source, "html.parser")
table_header = parse.find("tbody")

for rows in table_header:
    rows = table_header.find_all("tr")  # Note the use of find_all
    print(rows)
# data_table = table_header.find("tr")


for row in table_rows:
    data = row.find("td")  # Use find to find the first td element in each row
    print(data.text)
