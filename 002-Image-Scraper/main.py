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


def get_img_nodes(keyword=None, limit=10):
    if not keyword:
        raise Exception("Keyword is not given")

    base_url = "https://unsplash.com/s/photos/"
    url = f"{base_url}{keyword}?per_page={limit}"

    response = get(url)

    if response.status_code != 200:
        raise Exception("Request failed with status code " + str(response.status_code))

    tree = HTMLParser(response.text)
    imgs = tree.css("figure a img + div img")

    return imgs


def img_urls_filter(img_urls, no_list):
    filtered_urls = []
    for url in img_urls:
        if not any(word in url for word in no_list):
            filtered_urls.append(url)

    return filtered_urls


if __name__ == "__main__":
    img_nodes = get_img_nodes(keyword="water")
    img_urls = [i.attrs["src"] for i in img_nodes]
    print(len(img_urls))

    no_list = ["plus", "premium", "profile"]
    filtered_urls = img_urls_filter(img_urls, no_list)
    print(len(filtered_urls))
    print(filtered_urls)
