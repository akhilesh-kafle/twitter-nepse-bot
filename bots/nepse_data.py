import time
import datetime
from bs4 import BeautifulSoup
import requests
import json

def scrapping():
    site = "https://merolagani.com/LatestMarket.aspx"
    req = requests.get(site)

    soup = BeautifulSoup(req.text,'lxml')
    table = soup.find('table',{'class':'table table-hover live-trading sortable'})

    headers = [i.text for i in table.find_all('th')]

    data = [j for j in table.find_all('tr',{'class': ["decrease-row","increase-row","nochange-row"]})]
    scrapped_result = [{headers[index]:cell.text for index,cell in enumerate(row.find_all("td"))} for row in table.find_all("tr")]
    scrapped_result.remove({})
    return scrapped_result
scrapping()
