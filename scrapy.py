import requests
from bs4 import BeautifulSoup
import time


urls = ['https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-tre-srch', 'https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-tre-srch', 'https://finance.yahoo.com/quote/ABBV?p=ABBV&.tsrc=fin-tre-srch']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


for url in urls:
    html_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_page.content, 'lxml')

    print(soup.find('title').get_text())

    # header_info = soup.find_all("div", id='quote-header-info')[0]

    # stock_title = header_info.find('h1').get_text()
    # current_price = header_info.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)').find('span').get_text()

    table_info = soup.find_all('table', class_='W(100%)')[0].find_all('tr')

    for i in range(0, 8):
        heading = table_info[i].find_all('td')[0].get_text()
        value = table_info[i].find_all('td')[1].get_text()

        print(heading + "            :               " + value)

    print('---------------------------------------------------------------------')
    time.sleep(5)




    #
    # print(stock_title)
    # print(current_price)

