import json
from pprint import pprint

"""
Define Key information from JSON file.
"""

infile = 'data/geo-ipv4.json'


def define_continent_info():
    with open(infile, 'r') as f:
        continent_codes = []
        continent_names = []
        data = json.load(f)
        for item in data:
            cont_code = item['continent_code']
            cont_name = item['continent_name']
            if cont_code == None:
                continue
            else:
                continent_codes.append(cont_code)
                continent_names.append(cont_name)
        location_data = dict(zip(continent_codes, continent_names))
        pprint(location_data)


if __name__ == '__main__':
    infile = 'data/geo-ipv4.json'
    define_continent_info()