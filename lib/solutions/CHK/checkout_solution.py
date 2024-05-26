import re
from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    price_data = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }

    promo_data = {
        'A': {
            'count': 3,
            'price': 130,
        },
        'B': {
            'count': 2,
            'price': 45,
        },
    }

    def get_item_subtotal(sku: str, count: int) -> int:
        """Calculate subtotal for given item type (single SKU) and count."""
        # Account for any promotions by using mod


    # Check for illegal input (it's unclear for now if the string is just 'AAA' or e.g. comma-separated,
    # let's assume just SKUs themselves for now
    if re.search('[^ABCD]', skus):
        return -1

    counter = Counter(skus)

    return sum([get_item_subtotal(sku, counter[sku]) for sku in skus])





