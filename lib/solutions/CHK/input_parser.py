import re

def parse_input(path):
    with open(path) as input_file:
        price_data = {}
        promo_data = {}
        free_item_data = {}

        file_content = input_file.read()
        data = re.findall(r'\|\s+([A-Z])\s+\|\s+(\d+)\s+\|\s+(.*)\s+\|\n', file_content)
        skus, prices, promos_raw = zip(*data)

        for i in range(len(skus)):
            sku = skus[i]
            price = int(prices[i].strip())
            price_data[sku] = price

            promo_raw = promos_raw[i].strip()

    return price_data, promo_data, free_item_data


parse_input("./challenges/CHK_R4.txt")



