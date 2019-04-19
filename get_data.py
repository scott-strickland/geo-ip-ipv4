import requests
import json


response = requests.get('https://pkgstore.datahub.io/core/geoip2-ipv4/geoip2-ipv4_json/data/cf73950df86b88f44f13c2d95fb7609d/geoip2-ipv4_json.json')

data = response.json()

with open('geo-ipv4.json', 'w') as f:
    json.dump(data, f, indent=2)