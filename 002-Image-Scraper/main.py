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
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    )


# gets all the image tag nodes in the page
def get_img_nodes(keyword=None, limit=10):
    if not keyword:
        raise Exception("Keyword is not given")

    base_url = "https://unsplash.com/s/photos/"
    url = f"{base_url}{keyword}?per_page={limit}"

    response = get(url)

    if response.status_code != 200:
        raise Exception("Request failed with status code " + str(response.status_code))

    tree = HTMLParser(response.text)
    img_nodes = tree.css("figure a img + div img")

    return img_nodes


# filter out premium, watermarked images
def img_urls_filter(img_urls, no_list):
    filtered_urls = []
    for url in img_urls:
        url = url.split("?")[0] # strip out the parameters after ?
        if not any(word in url for word in no_list):
            filtered_urls.append(url)

    return filtered_urls


# download the images
def save_images(img_urls, save_folder="images", tag=""):
    for url in img_urls:
        response = get(url)
        logging.info(f"Downloading {url}")
        file_name = url.split("/")[-1]

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        with open(f"{save_folder}/{tag}_{file_name}.jpg", "wb") as f:
            f.write(response.content)
            logging.info(f"Saved {file_name}, size: {round(len(response.content) / 1024 / 1024, 2)} MB.")


if __name__ == "__main__":
    search_keyword = "water"

    img_nodes = get_img_nodes(keyword=search_keyword)
    img_urls = [i.attrs["src"] for i in img_nodes]

    no_list = ["plus", "premium", "profile"]
    filtered_urls = img_urls_filter(img_urls, no_list)

    save_images(img_urls=filtered_urls[:3], save_folder="images", tag=search_keyword)
