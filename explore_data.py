import json
import netaddr

"""
This was written in Python 3.7.2.  The purpose of this file is to explore the dataset of IPv4 geolocation from https://datahub.io/collections/reference-data#ipv4-geolocation.
"""

infile = 'geo-ipv4.json'
outfile = 'agg-ipv4.json'
cidr_list = []
net_list = []


with open(infile, 'r') as f:
    data = json.load(f)

for item in data:
    for k, v in item.items():
        if k == 'network':
            cidr_list.append(v)


cidr_range = netaddr.IPSet(cidr_list)
#net_list = json.dumps(cidr_range)

with open(outfile, 'w') as f:
    for cidr in cidr_range.iter_cidrs():
        net_list.append(str(cidr))
#        net_list = json.loads(net_list)
    json.dump(net_list, f, indent=2)
    
