# #### Section 06 - Project 1 - Portfolio Valuation With Google Finance
# - Project Scope
# 	- scrape price information from Google Finance, given some ticker and exchange
# 	- summarize portfolio valuation for an arbitrary number of positions
# 	- solution should reflect USD accounts only, but also support positions listed in other currencies i.e. should support some sort of FX-ing capability
# URL - https://www.google.com/finance/

import requests
from bs4 import BeautifulSoup


def extract_stock_price(headers, base_url, stock_ticker, stock_exchange):
    url = base_url + stock_ticker + ':' + stock_exchange
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    price_div = soup.find('div', {'data-last-price': True})
    price = float(price_div['data-last-price'])
    currency = price_div['data-currency-code']

    return {
        'Ticker': stock_ticker,
        'Exchange': stock_exchange,
        'Price': price,
        'Currency': currency
    }


def main():
    base_url = "https://www.google.com/finance/quote/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }

    print(extract_stock_price(headers, base_url,"TSLA", "NASDAQ"))


if __name__ == "__main__":
    main()
