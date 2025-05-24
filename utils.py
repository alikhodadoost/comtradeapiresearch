import json

def read_country_codes():
    with open('data/m49_codes.json', 'r') as f:
        return json.load(f)

def read_country_names():
    with open('data/m49_names.json', 'r') as f:
        return json.load(f)

def read_commodity_codes():
    with open('data/commodity_codes.json', 'r') as f:
        return json.load(f)

def read_commodity_names():
    with open('data/commodity_names.json', 'r') as f:
        return json.load(f)
    

def country_code_to_name(code: int):
    return read_country_names()[read_country_codes().index(code)]

def country_name_to_code(name: str):
    return read_country_codes()[read_country_names().index(name)]

def commodity_name_to_code(name: str):
    return read_commodity_codes()[read_commodity_names().index(name)]

# example usage
# codes = read_country_codes()
# print(codes[:5])

# names = read_country_names()
# print(names[:5])