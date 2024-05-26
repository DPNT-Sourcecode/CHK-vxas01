from collections import defaultdict

import re

def parse_input(path):
    with open(path) as input_file:
        price_data = {}
        promo_data = defaultdict(dict)
        free_item_data = defaultdict(dict)

        file_content = input_file.read()
        data = re.findall(r'\|\s+([A-Z])\s+\|\s+(\d+)\s+\|\s+(.*)\s+\|\n', file_content)
        skus, prices, promos_raw = zip(*data)

        for i in range(len(skus)):
            sku = skus[i]
            price = int(prices[i].strip())
            price_data[sku] = price

            promo_raw_items = promos_raw[i].strip().split(', ')

            for promo_str in promo_raw_items:
                if 'for' in promo_str:
                    # Regular promotion
                    quantity, sku, price = re.match(r'(\d+)([A-Z]) for (\d+)', promo_str)
                    promo_data[sku][int(quantity)] = int(price)
                else:
                    # Free item promotion
                    quantity, sku, price = re.match(r'(\d+)([A-Z]) for (\d+)', promo_str)
                    promo_data[sku][int(quantity)] = int(price)

    return price_data, promo_data, free_item_data


parse_input("./challenges/CHK_R4.txt")





