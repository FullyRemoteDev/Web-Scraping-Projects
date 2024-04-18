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

from utils.extract import extract_full_body_html
from selectolax.parser import HTMLParser

url = "https://store.steampowered.com/specials/"

if __name__ == "__main__":
    html = extract_full_body_html(
        from_url=url,
        wait_for='div[class*="y9MSdld4zZCuoQpRVDgMm"]'
    )

    tree = HTMLParser(html)

    divs = tree.css('div[class*="y9MSdld4zZCuoQpRVDgMm"]')
    print(len(divs))

    for div in divs:
        title = div.css_first('div[class*="StoreSaleWidgetTitle"]').text()
        thumbnail = div.css_first('div[class*="CapsuleImageCtn"] img').attributes.get("src")
        tags = [tag.text() for tag in div.css('a[class*="WidgetTag"]')[:5]]
        release_date = div.css_first('div[class*="_3eOdkTDYdWyo_U5-JPeer1"]').text()
        review_score = div.css_first('a[class*="ReviewScore"] div div').text()
        reviewed_by = div.css_first('div[class*="_1Deyvnxud-VpRoj0-ak-WK"]').text()
        
        sale_price = div.css_first('div[class*="Wh0L8EnwsPV_8VAu8TOYr"]').text()
        original_price = div.css_first('div[class*="_1EKGZBnKFWOr3RqVdnLMRN"]').text()


        attrs = {
            "title": title,
            "original_price": original_price,
            "sale_price": sale_price,
            "review_score": review_score,   
            "reviewed_by": reviewed_by,
            "release_date": release_date,
            "tags": tags,
            "thumbnail": thumbnail,
        }

        print(attrs)
