#!/usr/bin/python
import glob
import json
import re

# Files of my interest
selectedFiles = {
'SMpL3z4FLF07bRA6-y22JQ.json':None,
'SfrHdU4NCkYWvERnWaOUqQ.json':None,
'UL3OMN_c-NXHlyb97pDifA.json':None,
'URweBWkD1EgPDFUlL0LOKQ.json':None,
'UVBElUlajafZDSiBK2pltw.json':None,
'V9i9LnTg9H2XvzqCVBSOXg.json':None,
'VbXy3tH5RAu7HjT7VeMMgA.json':None,
'WUtPI9rJbs7ET1gPhULnDw.json':None,
'ZRJwVLyzEJq1VAihDhYiow.json':None,
'a1t31qMLd5fQocEjbSJ61A.json':None,
'aTwYIgWQUfoa2HobcjodTw.json':None,
'auorqdHiATGZHVd-sd79ZQ.json':None,
'cRfn_vMQ9YExuKb378CwjQ.json':None,
'efsZLHcgEn7hKGB05B569Q.json':None,
'f6KGn2OyYk6LWEpnUEgerw.json':None,
'fVgrpVyp-nPLTac9YIjTug.json':None,
'gEAB85-Zcm8Qs5JQPC_PHg.json':None,
'hVSuSlR4uYNnap2LU-6Tcg.json':None,
'iNvY0zAlaD_ye7Z6rHu-Ug.json':None,
'k8JnZBspVOI8kLcQek-Chw.json':None,
}

docs      = glob.glob('*.json')
outputDir = 'HindiTranslation/'

with open('My_Shortlisted_Restaurants.json', 'r') as f:
    business = json.load(f)

# Dump review and ratings in file
for doc in docs:
    if doc in selectedFiles:
        # Create a file in HindiTranslation by that name
        # Restautant Name
        restaurantName = business[doc[:-5]][0]
        inFile  = doc
        outFile = outputDir + restaurantName + '.txt'
        fhand   = open(inFile, 'r')
        output  = open(outFile, 'w')
        for line in fhand:
            data = json.dumps(line)
            review = data[data.find("'text':")+9: data.find("'business_id':")-2]
            rating = data[data.find("'stars':")+8:data.find("'date':")-2]
            review = review.strip('\"')
            review = review.strip("\\n\'")
            rating = rating.strip()
            data   = review + ' ##### ' + rating + '\n'
            output.write(data)
        # End of reading file
        fhand.close()
        output.close()
# End of reading all files of my interest
