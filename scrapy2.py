import requests
from bs4 import BeautifulSoup
url = 'https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
html_page = requests.get(url, headers=headers)
soup = BeautifulSoup(html_page.content, 'lxml')
table_info = soup.find_all('div', class_='entry-content')[0].find_all('tr')
th1 = table_info[0].find_all('th')[0].get_text()
th2 = table_info[0].find_all('th')[1].get_text()
th3 = table_info[0].find_all('th')[2].get_text()
print(th1, "----", th2, "----", th3)
for i in range(1, 7):
    td1 = table_info[i].find_all('td')[0].get_text()
    td2 = table_info[i].find_all('td')[1].get_text()
    td3 = table_info[i].find_all('td')[2].get_text()
    print(td1, "----", td2, "----", td3)






#
# print(stock_title)
# print(current_price)

