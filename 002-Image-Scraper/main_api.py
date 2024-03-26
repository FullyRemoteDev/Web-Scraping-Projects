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
import os


def get_response_for(keyword, results_per_page, page=1):
    base_url = "https://unsplash.com/napi/search/photos"
    url = f"{base_url}?query={keyword}&per_page={results_per_page}&page={page}"

    response = get(url)
    if response.status_code == 200:
        return response.json()


def get_image_urls(data):
    results = data["results"]

    full_img_urls = [x["urls"]["raw"] for x in results if x["premium"] is False]
    img_urls = [x.split("?")[0] for x in full_img_urls]

    return img_urls


def download_images(img_urls, max_download, save_folder="images", keyword=""):
    successfully_downloaded = 0

    for url in img_urls:
        if successfully_downloaded < max_download:
            response = get(url)
            file_name = keyword + "_" + url.split("/")[-1]

            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
            
            with open(f"{save_folder}/{file_name}.jpg", "wb") as f:
                f.write(response.content)
                successfully_downloaded += 1
        else:
            break

    return successfully_downloaded


def scrape(keyword, num_of_results):
    start_page = 1
    success_count = 0

    while success_count < num_of_results:
        data = get_response_for(keyword=keyword, results_per_page=20, page=start_page)

        max_downloads = num_of_results - success_count

        if data:
            img_urls = get_image_urls(data)
            success_downloads = download_images(img_urls, max_downloads, keyword=keyword)
            success_count += success_downloads
            start_page += 1
        else:
            print("Error: No data returned")
            break
        

if __name__ == "__main__":
    scrape("water", 10)