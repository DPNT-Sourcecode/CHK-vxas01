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
        'E': 40,
    }

    promo_data = {
        'A': {
            3: 130,
            5: 200,
        },
        'B': {
            2: 45,
        },
    }

    def get_item_subtotal(sku: str, count: int) -> int:
        """Calculate subtotal for given item type (single SKU) and count."""
        subtotal = 0

        # Account for any promotions by using mod
        if sku in promo_data:
            # Try to apply the best promotion (most items) first
            promo_counts = sorted(promo_data[sku].values(), reverse=True)

            for count in promo_counts:
                promo_packages = count // promo_data[sku]['count']
                subtotal += promo_packages * promo_data[sku]['price']
                count -= promo_packages * promo_data[sku]['count']

        subtotal += count * price_data[sku]

        return subtotal

    # Check for illegal input (it's unclear for now if the string is just 'AAA' or e.g. comma-separated,
    # let's assume just SKUs themselves for now
    if re.search('[^ABCDE]', skus):
        return -1

    counter = Counter(skus)

    return sum([get_item_subtotal(sku, counter[sku]) for sku in counter])




