# #### Section 06 - Project 1 - Portfolio Valuation With Google Finance
# - Project Scope
# 	- scrape price information from Google Finance, given some ticker and exchange
# 	- summarize portfolio valuation for an arbitrary number of positions
# 	- solution should reflect USD accounts only, but also support positions listed in other currencies i.e. should support some sort of FX-ing capability
# URL - https://www.google.com/finance/

import requests
from bs4 import BeautifulSoup


def convert_to_usd(headers, base_url, currency):
    url = f"{base_url}{currency}-USD"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    exchange_rate_div = soup.find("div", attrs={"data-last-price": True})
    exchange_rate = float(exchange_rate_div["data-last-price"])

    return exchange_rate


def extract_stock_info(headers, base_url, stock_ticker, stock_exchange):
    url = base_url + stock_ticker + ":" + stock_exchange
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    price_div = soup.find("div", attrs={"data-last-price": True})
    price = float(price_div["data-last-price"])
    currency = price_div["data-currency-code"]

    price_in_usd = price
    if currency != "USD":
        exchange_rate = convert_to_usd(headers, base_url, currency)
        price_in_usd = round(price * exchange_rate, 2)

    return {
        "Ticker": stock_ticker,
        "Exchange": stock_exchange,
        "Price": price_in_usd,
        "Currency": currency,
    }


def main():
    base_url = "https://www.google.com/finance/quote/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }

    print(extract_stock_info(headers, base_url, "TSLA", "NASDAQ"))
    print(extract_stock_info(headers, base_url, "SHOP", "TSE"))


if __name__ == "__main__":
    main()
