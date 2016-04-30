# -*- coding: utf-8 -*-
import os
dir = "IAAgreement"
IAA = {'Pankaj':{},'Kush':{}}
agreement = 0
pPos = 0
kPos = 0
pNeg = 0
kNeg = 0
total = 0
pospos = 0
posneg = 0
negpos = 0
negneg = 0
for i in os.listdir("IAAgreement"):
    if i.endswith(".txt"):
        with open("IAAgreement\\"+i) as f:
            for line in f:
                total += 1
                line = line.decode('utf-8')
                l = line.split(u"।")
                if len(l) == 0:
                    l = line.split(u"!")
                val = l[1].split('##')
                IAA['Pankaj'] = val[0].strip()
                IAA['Kush'] = val[1].strip()
                if IAA['Pankaj'] == IAA['Kush']:
                    agreement += 1

                if IAA['Pankaj'] == 'POSITIVE':
                    pPos += 1
                    if IAA['Kush'] == 'POSITIVE':
                        pospos += 1
                    else:
                        posneg += 1
                elif IAA['Pankaj'] == 'NEGATIVE':
                    pNeg += 1
                    if IAA['Kush'] == 'POSITIVE':
                        negpos += 1
                    else:
                        negneg += 1
                if IAA['Kush'] == 'POSITIVE':
                    kPos += 1
                elif IAA['Kush'] == 'NEGATIVE':
                    kNeg += 1
Ae = (float(pPos) / float(total) * float(kPos) / float(total)) + (float(pNeg) / float(total) * float(kNeg) / float(total))
Ao = float(agreement) / float(total)
Kappa = (Ao - Ae) / (1 - Ae)
print pPos+pNeg
print kPos+kNeg
print total
print Kappa

print Ae
print Ao

print 'pospos: ' + str(pospos)
print 'posneg: ' + str(posneg)
print 'negpos: ' + str(negpos)
print 'negneg: ' + str(negneg)

print pospos + posneg + negpos + negneg