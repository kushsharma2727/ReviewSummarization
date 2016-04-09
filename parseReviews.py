#!/usr/bin/python

import os
import sys
import re
import json
import glob
import simplejson

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)
PANKAJ = dict()
with open('My_Shortlisted_Restaurants.json', 'r') as f:
    RESTAURANTS = json.load(f)

def grabJSON(s):
    decoder = simplejson.JSONDecoder()
    obj, end = decoder.raw_decode(s)
    end = WHITESPACE.match(s, end).end()
    return obj, s[end:]

def getData(docs):
    fname = 'My_Final_Reviews_Yelp.json'
    fhand = open(fname, 'w')
    for doc in docs:
        with open(doc) as f:
            s = f.read()

        while True:
            obj, remaining = grabJSON(s)
            if obj['business_id'] in RESTAURANTS:
                PANKAJ[obj['business_id']] = PANKAJ.get(obj['business_id'], 0) + 1
                fhand.write(str(obj))

            s = remaining
            if not remaining.strip():
                break

        f.close()

    fhand.close()
    for key, value in PANKAJ.items():
        print key, value

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
    path = path + '/Reviews'
    docs = glob.glob(path + '/*.json')
    getData(docs)

# Preconditions:
# My_Shortlisted_Restaurants contains ID's of all restaurants of our interest
# Review contains all the json files where we are searching for reviews.
# I split large dataset into bunch of files and manually corrected the json
# format errors.
if __name__ == '__main__':
    main()

