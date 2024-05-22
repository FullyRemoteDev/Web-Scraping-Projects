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
from utils.parse import parse_raw_attributes
from utils.process import format_and_transform
from config.tools import load_config
from selectolax.parser import HTMLParser


if __name__ == "__main__":
    config = load_config()

    html = extract_full_body_html(
        from_url=config.get("url"),
        wait_for=config.get("container").get("selector")
    )

    tree = HTMLParser(html)
    divs = tree.css(config.get("container").get("selector"))
    print(len(divs))

    for div in divs:
        attrs = parse_raw_attributes(div, config.get("item"))
        attrs = format_and_transform(attrs)

        # post-processing notes:
        
        # title -> nothing
        # review_score -> nothing

        # thumbnail -> attr.src
        # tags -> first 5 from list
        # release_date -> reformatted to yyyy-mm-dd
        # reviewed_by -> extract digits only
        # price_currency -> split by space, get first
        # sale_price -> split by space, get second     
        # original_price -> split by space, get second     


        # {'title': 'V Rising', 'thumbnail': <Node img>, 'tags': ['Survival', 'Open World', 'Base Building', 'Vampire', 'Multiplayer', 'Crafting', 'Online Co-Op', 'PvP', 'PvE', 'Building', 'Hack and Slash', 'Sandbox', 'Exploration', 'Massively Multiplayer', 'Action', 'Action-Adventure', 'Singleplayer', 'Adventure', 'Dark Fantasy', 'Co-op'], 'release_date': 'May 8, 2024', 'review_score': 'Very Positive', 'reviewed_by': '| 75,031 User Reviews', 'price_currency': '₹1,350.00', 'sale_price': '₹1,350.00', 'original_price': '₹1,500.00'}


        # title = div.css_first('div[class*="StoreSaleWidgetTitle"]').text()
        # thumbnail = div.css_first('div[class*="CapsuleImageCtn"] img').attributes.get("src")
        # tags = [tag.text() for tag in div.css('a[class*="WidgetTag"]')[:5]]
        # release_date = div.css_first('div[class*="_3eOdkTDYdWyo_U5-JPeer1"]').text()
        # review_score = div.css_first('a[class*="ReviewScore"] div div').text()
        # reviewed_by = div.css_first('div[class*="_1Deyvnxud-VpRoj0-ak-WK"]').text()
        
        # sale_price = div.css_first('div[class*="Wh0L8EnwsPV_8VAu8TOYr"]').text()
        # original_price = div.css_first('div[class*="_1EKGZBnKFWOr3RqVdnLMRN"]').text()


        # attrs = {
        #     "title": title,
        #     "original_price": original_price,
        #     "sale_price": sale_price,
        #     "review_score": review_score,   
        #     "reviewed_by": reviewed_by,
        #     "release_date": release_date,
        #     "tags": tags,
        #     "thumbnail": thumbnail,
        # }

        print(attrs)
