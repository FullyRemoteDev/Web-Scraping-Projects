# Scope Statement
#   - write a python script that scrapes images from Unsplash
#   - https://unsplash.com
#   - the utility should download the highest resolution image that
#     pertains to a given keyword
#   - premium, watermarked images should be excluded
#   - for extra practice, explore HTML-based scraping in addition to the
#     API-based route
#   - sample interface
#       if __name__ == "__main__":
#           scrape("water", 10)
# 

import requests
from selectolax.parser import HTMLParser


def scrape(base_url, keyword, limit=10):
    pass


if __name__ == "__main__":
    base_url = "https://unsplash.com/s/photos/"
    scrape(base_url, "water")
