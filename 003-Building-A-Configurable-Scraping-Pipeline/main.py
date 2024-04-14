# - Scope Statement
# 	- Learning Outcome #1
# 		- JavaScript Scraping with Playwright
# 		- https://store.steampowered.com/specials
# 			- title
# 			- link to thumbnail
# 			- category tags
# 			- rating
# 			- number of reviews
# 			- original price
# 			- discounted price
# 			- discount %

from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

url = "https://store.steampowered.com/specials/"

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        page.wait_for_load_state("networkidle")
        page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_selector('div[class*="y9MSdld4zZCuoQpRVDgMm"]')

        html = page.inner_html("body")
        tree = HTMLParser(html)

        divs = tree.css('div[class*="y9MSdld4zZCuoQpRVDgMm"]')
        print(len(divs))

        for div in divs:
            title = div.css_first('div[class*="StoreSaleWidgetTitle"]').text()
            thumbnail = div.css_first('div[class*="CapsuleImageCtn"] img').attributes.get("src")
            tags = [tag.text() for tag in div.css('a[class*="WidgetTag"]')[:5]]
            release_date = div.css_first('div[class*="_3eOdkTDYdWyo_U5-JPeer1"]').text()
            reviewed_by = div.css_first('div[class*="_1Deyvnxud-VpRoj0-ak-WK"]').text()

            attrs = {
                "title": title,
                "reviewed_by": reviewed_by,
                "release_date": release_date,
                "tags": tags,
                "thumbnail": thumbnail,
            }

            print(attrs)

