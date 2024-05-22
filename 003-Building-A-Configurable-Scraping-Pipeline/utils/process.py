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


def format_and_transform(attrs: dict):
    transforms = {
        "thumbnail": lambda n: get_attrs_from_node(n, "src"),
        "tags": lambda input_list: get_first_n(input_list, 5),
        "release_date": lambda date: reformat_date(date, '%b %d, %Y', '%Y-%m-%d')
    }

    for k, v in transforms.items():
        if k in attrs:
            attrs[k] = v(attrs[k])
            
    return attrs

