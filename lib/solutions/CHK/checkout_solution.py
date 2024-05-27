import re
from collections import Counter

from .input_parser import parse_input


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # price_data = {
    #     'A': 50,
    #     'B': 30,
    #     'C': 20,
    #     'D': 15,
    #     'E': 40,
    #     'F': 10,
    # }
    #
    # promo_data = {
    #     'A': {
    #         3: 130,
    #         5: 200,
    #     },
    #     'B': {
    #         2: 45,
    #     },
    # }
    #
    # free_item_data = {
    #     'E': {
    #         2: 'B',
    #     },
    #     'F': {
    #         3: 'F',
    #     }
    # }

    path = "./challenges/CHK_R5.txt"
    price_data, promo_data, free_item_data, group_promo_data = parse_input(path)

    def get_item_subtotal(sku: str, count: int) -> int:
        """Calculate subtotal for given item type (single SKU) and count."""
        subtotal = 0

        # Account for any promotions by using mod
        if sku in promo_data:
            # Try to apply the best promotion (most items) first
            promos = sorted(promo_data[sku].items(), reverse=True)

            for promo_count, promo_price in promos:
                promo_packages = count // promo_count
                subtotal += promo_packages * promo_price
                count -= promo_packages * promo_count

        subtotal += count * price_data[sku]

        return subtotal

    # Check for illegal input (it's unclear for now if the string is just 'AAA' or e.g. comma-separated,
    # let's assume just SKUs themselves for now
    if re.search(f"[^{''.join(price_data.keys())}]", skus):
        return -1

    total = 0
    counter = Counter(skus)

    # Apply free items before other promos
    for sku in list(counter.keys()):
        count = counter.get(sku, 0)

        if sku in free_item_data:
            promos = sorted(free_item_data[sku].items(), reverse=True)

            for promo_count, reward in promos:
                reward_counter = Counter(reward)
                promo_packages = count // promo_count

                for i in range(promo_packages):
                    counter -= reward_counter

    # Apply group promotions before individual ones
    for sku_group, promo_data in group_promo_data.items():
        promo_count, promo_price = promo_data.items()[0]
        match_counter = {}  # Can't use Counter here, because it breaks ordering

        for sku in sku_group:
            match_counter[sku] = counter[sku]

        while sum(match_counter.values()) >= promo_count:
            # Reduce in batches of size == promo_count
            for i in range(promo_count):
                

            total += promo_price

    return sum([total] + [get_item_subtotal(sku, counter[sku]) for sku in counter])





