#!/usr/bin/env python

import requests


def main():
    data = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()
    cidrs = (p['ip_prefix'] for p in data['prefixes'] if p['service'] == 'CLOUDFRONT')
    for cidr in cidrs:
        print('set_real_ip_from {};'.format(cidr))


main()
