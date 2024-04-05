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

url = "https://store.steampowered.com/specials/"

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        page.wait_for_load_state("networkidle")
        page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")

        print(page.title())       


