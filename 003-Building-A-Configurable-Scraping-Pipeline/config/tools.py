import json


_config = {
    "url": "https://store.steampowered.com/specials/",
    "meta": {
        "name": "Steam Sales Scraper",
        "description": "Extracts the highest discounted games from Steam.",
        "author": "FullyRemoteDev",
        "version": 0.1
    },
    "container": {
        "name": "store_sale_divs",
        "selector": "div[class*='y9MSdld4zZCuoQpRVDgMm']",
        "match": "all",
        "type": "node",
    },
    "item": [
        {
            "name": "title",
            "selector": "div[class*=\"StoreSaleWidgetTitle\"]",
            "match": "first",
            "type": "text",
        },
        {
            "name": "thumbnail",
            "selector": "div[class*=\"CapsuleImageCtn\"] img",
            "match": "first",
            "type": "node",
        },
        {
            "name": "tags",
            "selector": "a[class*=\"WidgetTag\"]",
            "match": "all",
            "type": "text",
        },
        {
            "name": "release_date",
            "selector": "div[class*=\"_3eOdkTDYdWyo_U5-JPeer1\"]",
            "match": "first",
            "type": "text",
        },
        {
            "name": "review_score",
            "selector": "a[class*=\"ReviewScore\"] div div",
            "match": "first",
            "type": "text",
        },
        {
            "name": "reviewed_by",
            "selector": "div[class*=\"_1Deyvnxud-VpRoj0-ak-WK\"]",
            "match": "first",
            "type": "text",
        },
        {
            "name": "price_currency",
            "selector": "div[class*=\"Wh0L8EnwsPV_8VAu8TOYr\"]",
            "match": "first",
            "type": "text",
        },
        {
            "name": "sale_price",
            "selector": "div[class*=\"Wh0L8EnwsPV_8VAu8TOYr\"]",
            "match": "first",
            "type": "text",
        },
        {
            "name": "original_price",
            "selector": "div[class*=\"_1EKGZBnKFWOr3RqVdnLMRN\"]",
            "match": "first",
            "type": "text",
        },
    ],
}


def load_config(from_file=False):
    if from_file:
        with open("config/config.json", "r") as f:
            return json.load(f)
    return _config


def generate_config():
    with open("config/config.json", "w") as f:
        json.dump(_config, f, indent=4)


if __name__ == "__main__":
    generate_config()
