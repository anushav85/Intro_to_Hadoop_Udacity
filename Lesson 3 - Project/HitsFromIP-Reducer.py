#!/usr/bin/python

import sys

totalHits = 0
oldIP = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisIP, thisPage = data_mapped

    if oldIP and oldIP != thisIP:
        print oldIP, "\t", totalHits
        oldIP = thisIP;
        totalHits = 0

    oldIP = thisIP
    totalHits += 1

if oldIP != None:
    print oldIP, "\t", totalHits
