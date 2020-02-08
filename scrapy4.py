import requests
from bs4 import BeautifulSoup
import time
import csv


urls = ['https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch', 'https://finance.yahoo.com/quote/MRNA?p=MRNA&.tsrc=fin-tre-srch', 'https://finance.yahoo.com/quote/FDX?p=FDX&.tsrc=fin-tre-srch', 'https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-tre-srch', 'https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-tre-srch', 'https://finance.yahoo.com/quote/ABBV?p=ABBV&.tsrc=fin-tre-srch']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Comapny name', 'Previous Close', 'Open', 'Bid', 'Ask', "Day's Range", '52 Week Range', 'Volume', 'Avg. Volume'])


for url in urls:
    stock = []
    html_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_page.content, 'lxml')
    stock.append(soup.find('title').get_text())
    # stock.append(soup.find('My(6px) Pos(r) smartphone_Mt(6px)')[0].find_all('span')[0].get_text())
    table_info = soup.find_all('table', class_='W(100%)')[0].find_all('tr')



    for i in range(0, 8):
        value = table_info[i].find_all('td')[1].get_text()
        stock.append(value)
    csv_writer.writerow(stock)