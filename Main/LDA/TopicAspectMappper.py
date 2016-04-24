# -*- coding: utf-8 -*-
import os

topicsAspectMap = {}
# topicsAspectMap['0'] = "Food"
# topicsAspectMap['1'] = "Food"
# topicsAspectMap['2'] = "Service"
# topicsAspectMap['3'] = "Ambience"
# topicsAspectMap['4'] = "Food"
# topicsAspectMap['5'] = "Service"
# topicsAspectMap['6'] = "Value"
# topicsAspectMap['7'] = "Service"
# topicsAspectMap['8'] = "Food"
# topicsAspectMap['9'] = "Ambience"
# topicsAspectMap['10'] = "Food"
# topicsAspectMap['11'] = "Ambience"

topicsAspectMap['0'] = "Food"
topicsAspectMap['1'] = "Food"
topicsAspectMap['2'] = "xyz"
topicsAspectMap['3'] = "Food"
topicsAspectMap['4'] = "Ambience"
topicsAspectMap['5'] = "Service"
topicsAspectMap['6'] = "abc"
topicsAspectMap['7'] = "Service"
topicsAspectMap['8'] = "pqr"

path = "op1"
directory = "output"
if not os.path.exists(directory):
    os.makedirs(directory)

for i in os.listdir("op1"):
    with open("op1\\"+i) as f:
        opPath = directory+'\\'+i.rstrip('.txt')
        if not os.path.exists(opPath):
            os.makedirs(opPath)
        o = open(opPath+'\\'+i, 'w')
        for line in f:
            l = line.split('#####')
            if len(l) > 1:
                w = l[0]+'#####'+topicsAspectMap[l[1].rstrip('\n')]
                o.write(w+'\n')
        o.close()