#!/usr/bin/python
import sys
Max = 0
oldKey = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue

	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey,Max)
		Max = 0
	oldKey = thisKey
	x = float(thisSale)
	if Max < x:
		Max = x
if oldKey != None:
	print oldKey,"\t", Max


