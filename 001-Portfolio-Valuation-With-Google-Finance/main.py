# #### Section 06 - Project 1 - Portfolio Valuation With Google Finance
# - Project Scope
# 	- scrape price information from Google Finance, given some ticker and exchange
# 	- summarize portfolio valuation for an arbitrary number of positions
# 	- solution should reflect USD accounts only, but also support positions listed in other currencies i.e. should support some sort of FX-ing capability
# URL - https://www.google.com/finance/

import requests
from bs4 import BeautifulSoup


base_url = 'https://www.google.com/finance/quote/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

stock_ticker = 'TSLA'
stock_exchange = 'NASDAQ'

url = base_url + stock_ticker + ':' + stock_exchange
response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, 'lxml')

print(soup.prettify())
