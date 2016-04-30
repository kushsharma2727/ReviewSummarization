#!/usr/bin/python
# -*- coding: utf-8 -*-
fhand = open('final.txt', 'r')

zeros= 0
ones = 0
twos = 0
while True:
    line = fhand.readline()
    if not line:
        break
    line = line.decode('utf-8').strip()
    line = line.split('##')
    score = int(line[1].strip())
    if score == 0:
        zeros += 1
    elif score == 1:
        ones += 1
    else:
        twos += 1
print 'ZERO:', zeros
print 'ONES:', ones
print 'TWOS:', twos
