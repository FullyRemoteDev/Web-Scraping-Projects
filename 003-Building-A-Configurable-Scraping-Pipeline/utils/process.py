from selectolax.parser import Node


def get_attrs_from_node(node: Node, attr: str):
    if node is None or not issubclass(Node, type(node)):
        raise ValueError("The function expects a selectolax node")
    
    return node.attributes.get(attr)


def get_first_n(input_list: list, n: int=5):
    return input_list[:n]


def format_and_transform(attrs: dict):
    transforms = {
        "thumbnail": lambda n: get_attrs_from_node(n, "src"),
        "tags": lambda input_list: get_first_n(input_list, 5)
    }

    for k, v in transforms.items():
        if k in attrs:
            attrs[k] = v(attrs[k])
            
    return attrs

