# #### Section 06 - Project 1 - Portfolio Valuation With Google Finance
# - Project Scope
# 	- scrape price information from Google Finance, given some ticker and exchange
# 	- summarize portfolio valuation for an arbitrary number of positions
# 	- solution should reflect USD accounts only, but also support positions listed in other currencies i.e. should support some sort of FX-ing capability
# URL - https://www.google.com/finance/

import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from tabulate import tabulate


@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = "USD"
    price_in_usd: float = 0

    def __post_init__(self):
        price_info = extract_stock_info(self.ticker, self.exchange)

        if price_info["ticker"] == self.ticker:
            self.price = price_info["price"]
            self.currency = price_info["currency"]
            self.price_in_usd = price_info["price_in_usd"]


@dataclass
class Position:
    stock: Stock
    quantity: int


@dataclass
class Portfolio:
    positions: list[Position]

    def portfolio_value(self):
        total_value = 0
        for position in self.positions:
            total_value += position.stock.price_in_usd * position.quantity
        return total_value


def convert_to_usd(currency):
    base_url = "https://www.google.com/finance/quote/"
    url = f"{base_url}{currency}-USD"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    exchange_rate_div = soup.find("div", attrs={"data-last-price": True})
    exchange_rate = float(exchange_rate_div["data-last-price"])

    return exchange_rate


def extract_stock_info(ticker, exchange):
    base_url = "https://www.google.com/finance/quote/"
    url = base_url + ticker + ":" + exchange
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    price_div = soup.find("div", attrs={"data-last-price": True})
    price = float(price_div["data-last-price"])
    currency = price_div["data-currency-code"]

    price_in_usd = price
    if currency != "USD":
        exchange_rate = convert_to_usd(currency)
        price_in_usd = round(price * exchange_rate, 2)

    return {
        "ticker": ticker,
        "exchange": exchange,
        "price": price,
        "currency": currency,
        "price_in_usd": price_in_usd,
    }


def portfolio_display(portfolio):
    if not isinstance(portfolio, Portfolio):
        raise TypeError("portfolio should be of type Portfolio")

    portfolio_value = portfolio.portfolio_value()
    position_data = []

    print("\nPortfolio Positions:")

    for position in portfolio.positions:
        position_value = position.quantity * position.stock.price_in_usd
        position_percent = (position_value / portfolio_value) * 100
        position_data.append(
            [
                position.stock.ticker,
                position.stock.exchange,
                position.quantity,
                position.stock.price_in_usd,
                position_value,
                position_percent,
            ]
        )

        position_data = sorted(
            position_data,
            key=lambda x: x[4],
            reverse=True,
        )

    table_headers = [
        "Ticker",
        "Exchange",
        "Quantity",
        "Price (USD)",
        "Value (USD)",
        "%",
    ]

    print(
        tabulate(
            position_data,
            table_headers,
            tablefmt="fancy_grid",
            floatfmt=".2f",
        )
    )

    print(f"TotalPortfolio Value: ${portfolio_value:,.2f}\n")


if __name__ == "__main__":
    shop = Stock("SHOP", "TSE")
    msft = Stock("MSFT", "NASDAQ")
    tsla = Stock("TSLA", "NASDAQ")
    googl = Stock("GOOGL", "NASDAQ")

    portfolio = Portfolio([Position(shop, 50), Position(msft, 15), Position(tsla, 100), Position(googl, 50)])

    portfolio_display(portfolio)
