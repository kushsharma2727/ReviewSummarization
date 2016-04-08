#!/usr/bin/python

import os
import sys
import re
import json
import simplejson

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)
ID_COLLECTION = dict()

def grabJSON(s):
    decoder = simplejson.JSONDecoder()
    obj, end = decoder.raw_decode(s)
    end = WHITESPACE.match(s, end).end()
    return obj, s[end:]

def getData(path):
    i = 1
    with open(path) as f:
        s = f.read()

    while True:
        obj, remaining = grabJSON(s)
        categories = obj['categories']
        if obj["review_count"] > 200 and "Restaurants" in categories:
		ID_COLLECTION[obj["business_id"]] = (obj["name"], obj["review_count"])
                print i
                i += 1
        s = remaining
        if not remaining.strip():
            break

def getPath():
    if len(sys.argv) == 1:
        #Get the path to current directory
        path = os.getcwd()
    else:
        path = sys.argv[1]
    # Return the result to the caller
    return path

def main():
    path = getPath()
    path = path + '/yelp_academic_dataset_business.json'
    getData(path)
    with open('My_Business_Collection_Restaurants.json', 'w') as f:
	json.dump(ID_COLLECTION, f)

if __name__ == '__main__':
    main()
