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
from utils.process import format_and_transform, save_to_file
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

    game_data = []
    for div in divs:
        attrs = parse_raw_attributes(div, config.get("item"))
        attrs = format_and_transform(attrs)
        game_data.append(attrs)
        
        save_to_file("extract", game_data)
