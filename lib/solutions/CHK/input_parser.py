import re

def parse_input(path):
    with open(path) as input_file:
        file_content = input_file.read()
        data = re.findall(r'\|\s+([A-Z])\s+\|\s+(\d+)\s+\|\s+(.*)\s+\|\n', file_content)

        print(data)
        print(len(data))

parse_input("./challenges/CHK_R4.txt")

