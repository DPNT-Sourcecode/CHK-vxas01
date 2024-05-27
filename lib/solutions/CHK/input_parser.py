from collections import defaultdict

import re

def parse_input(path):
    with open(path) as input_file:
        price_data = {}
        promo_data = defaultdict(dict)
        free_item_data = defaultdict(dict)
        group_promo_data = defaultdict(dict)

        file_content = input_file.read()
        data = re.findall(r'\|\s+([A-Z])\s+\|\s+(\d+)\s+\|\s+(.*)\s+\|\n', file_content)
        skus, prices, promos_raw = zip(*data)

        for i in range(len(skus)):
            sku = skus[i]
            price = int(prices[i].strip())
            price_data[sku] = price

            promo_raw_items = promos_raw[i].strip().split(', ')

            for promo_str in promo_raw_items:
                if 'buy any' in promo_str:
                    # Mixed items promotion
                    quantity, sku, price = \
                        re.match(r'buy any (\d+) of \(([A-Z,]*)\) for (\d+)', promo_str).groups()
                    group_promo_data[sku][int(quantity)] = int(price)
                elif 'for' in promo_str:
                    # Regular promotion
                    quantity, sku, price = re.match(r'(\d+)([A-Z]) for (\d+)', promo_str).groups()
                    promo_data[sku][int(quantity)] = int(price)
                elif 'get one' in promo_str:
                    # Free item promotion
                    quantity, sku, reward = re.match(r'(\d+)([A-Z]) get one ([A-Z]) free', promo_str).groups()

                    # We need to account for same-sku free item promotions
                    if sku == reward:
                        quantity = int(quantity) + 1

                    free_item_data[sku][int(quantity)] = reward

        # Modify the keys of group_promo_data to include items in decreasing price order
        new_group_promo_data = {}

        for key in group_promo_data:
            skus = key.split(',')
            skus.sort(key=lambda sku: price_data[sku], reverse=True)
            new_group_promo_data[''.join(skus)] = group_promo_data[key]

    return price_data, promo_data, free_item_data, new_group_promo_data
