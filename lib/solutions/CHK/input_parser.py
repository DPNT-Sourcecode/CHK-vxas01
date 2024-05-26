import re

def parse_input(path):
    with open(path) as input_file:
        print(input_file.read())


parse_input("./challenges/CHK_R4.txt")
