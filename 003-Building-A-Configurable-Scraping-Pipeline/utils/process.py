import re
import pandas as pd
from datetime import datetime
from selectolax.parser import Node


def get_attrs_from_node(node: Node, attr: str):
    if node is None or not issubclass(Node, type(node)):
        raise ValueError("The function expects a selectolax node")
    
    return node.attributes.get(attr)


def get_first_n(input_list: list, n: int = 5):
    return input_list[:n]


def reformat_date(date_raw: str, input_format: str = '%b %d, %Y', output_format: str = '%Y-%m-%d'):
    dt_obj = datetime.strptime(date_raw, input_format)
    dt_fmt = datetime.strftime(dt_obj, output_format)
    return dt_fmt


def regex(input_str: str, pattern: str, do_what: str = "findall"):
    if do_what == "findall":
        return re.findall(pattern, input_str)
    else:
        raise ValueError("The function expects 'findall' or 'split' to be provided.")


def split(input_str: str, select_what: str = "price"):
    if select_what == "currency":
        return input_str[0]
    elif select_what == "price":
        return input_str[1:]


def format_and_transform(attrs: dict):
    transforms = {
        "thumbnail": lambda n: get_attrs_from_node(n, "src"),
        "tags": lambda input_list: get_first_n(input_list, 5),
        "release_date": lambda date: reformat_date(date, '%b %d, %Y', '%Y-%m-%d'),
        "reviewed_by": lambda raw: int(''.join(regex(raw, r'\d+', "findall"))),
        "price_currency": lambda raw: split(raw, "currency"),
        "sale_price": lambda raw: float(split(raw, "price").replace(",", "")),
        "original_price": lambda raw: float(split(raw, "price").replace(",", ""))
    }

    for k, v in transforms.items():
        if k in attrs:
            attrs[k] = v(attrs[k])
            
    return attrs


def save_to_file(filename="extract", data: list[dict] = None):
    if data is None:
        raise ValueError("The function expects data to be provided as a list of dictionaries.")
    
    df = pd.DataFrame(data)
    filename = f"{datetime.now().strftime('%Y_%m_%d')}_{filename}.csv"
    df.to_csv(filename, encoding='utf-8', index=False)
