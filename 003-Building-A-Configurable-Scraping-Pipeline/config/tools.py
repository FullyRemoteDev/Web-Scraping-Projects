import json


_config = {
    "url": "https://store.steampowered.com/specials/",
    "container": {
        "name": "store_sale_divs",
        "selector": "div[class*='y9MSdld4zZCuoQpRVDgMm']",
        "match": "all",
        "type": "node",
    },
    "items": [
        {
            "name": "title",
            "selector": "div[class*='y9MSdld4zZCuoQpRVDgMm']",
            "match": "first",
            "type": "text",
        }
    ]
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
