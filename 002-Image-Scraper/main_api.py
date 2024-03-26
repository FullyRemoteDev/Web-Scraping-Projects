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


def get_response_for(keyword, results_per_page):
    base_url = "https://unsplash.com/napi/search/photos"
    url = f"{base_url}?query={keyword}&per_page={results_per_page}"

    response = get(url)
    if response.status_code == 200:
        return response.json()


def get_image_urls(data):
    results = data["results"]

    full_img_urls = [x["urls"]["raw"] for x in results if x["premium"] is False]
    img_urls = [x.split("?")[0] for x in full_img_urls]

    return img_urls


if __name__ == "__main__":
    data = get_response_for("water", 10)

    img_urls = get_image_urls(data)
    print(img_urls)
