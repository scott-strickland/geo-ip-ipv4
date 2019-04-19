import json
import netaddr

"""
This was written in Python 3.7.2.  The purpose of this file is to explore the dataset of IPv4 geolocation from https://datahub.io/collections/reference-data#ipv4-geolocation.
"""


def load_data():
    """Load the raw geo IPv4 data from JSON."""
    with open(infile, 'r') as f:
        data = json.load(f)
    for item in data:
        for k, v in item.items():
            if k == 'network':
                cidr_list.append(v)
    return cidr_list


def write_data(cidr_list):
    """Write the extracted data to a new JSON file."""
    cidr_range = netaddr.IPSet(cidr_list)
    with open(outfile, 'w') as f:
        for cidr in cidr_range.iter_cidrs():
            net_list.append(str(cidr))
        json.dump(net_list, f, indent=2)


if __name__ == '__main__':
    infile = 'data/geo-ipv4.json'
    outfile = 'data/agg-ipv4.json'
    cidr_list = []
    net_list = []
    load_data()
    write_data(cidr_list)

    