import json
import netaddr
import sys

"""
This was written in Python 3.7.2.  The purpose of this file is to explore the dataset of IPv4 geolocation from https://datahub.io/collections/reference-data#ipv4-geolocation.
"""


def select_continent(code):
    """Select the continent by code."""
    for item in data:
        cont_code = item['continent_code']
        if cont_code == code:
            for k, v in item.items():
                load_data(k, v)


def load_data(k, v):
    """Load the raw geo IPv4 data from JSON."""
#    for k, v in item.items():
    if k == 'network':
        cidr_list.append(v)
    return cidr_list



def write_data(cidr_list):
    """Write the extracted data to a new JSON file."""
    cidr_range = netaddr.IPSet(cidr_list)
    for cidr in cidr_range.iter_cidrs():
        net_list.append(str(cidr))
    json.dump(net_list, f, indent=2)


if __name__ == '__main__':
    #outfile = 'data/sa-agg-ipv4.json'
    cidr_list = []
    net_list = []
    code = sys.argv[1].upper()
    infile = 'data/geo-ipv4.json'
    outfile = 'data/' + code + '-agg-ipv4.json'
    with open(infile, 'r') as f:
        data = json.load(f)
        #load_data()
        select_continent(code)
    with open(outfile, 'w') as f:
        write_data(cidr_list)
