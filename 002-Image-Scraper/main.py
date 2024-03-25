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


from httpx import get
from selectolax.parser import HTMLParser


def get_img_tags(keyword, limit=10):
    base_url = "https://unsplash.com/s/photos/"
    url = f"{base_url}{keyword}?per_page={limit}"

    response = get(url)

    if response.status_code != 200:
        raise Exception("Request failed with status code " + str(response.status_code))

    tree = HTMLParser(response.text)
    imgs = tree.css("figure a img + div img")

    return imgs


if __name__ == "__main__":
    print(get_img_tags("water"))
