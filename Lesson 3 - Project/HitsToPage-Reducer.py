#!/usr/bin/python

import sys

totalHits = 0
oldPage = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisPage, thisIP = data_mapped

    if oldPage and oldPage != thisPage:
        print oldPage, "\t", totalHits
        oldPage = thisPage;
        totalHits = 0

    oldPage = thisPage
    totalHits += 1

if oldPage != None:
    print oldPage, "\t", totalHits
