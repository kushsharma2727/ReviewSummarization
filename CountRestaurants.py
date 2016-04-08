#!/usr/bin/python

import json
with open('My_Shortlisted_Restaurants.json', 'r') as f:
    data = json.load(f)
print 'LEN: ', len(data)
