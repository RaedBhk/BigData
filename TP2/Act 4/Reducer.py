#!/usr/bin/python
import sys
salesTotal = 0
oldKey = None
day=None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 3:
		continue

	thisKey,thisDay, thisSale = data
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}\t{2}".format(oldKey,day,salesTotal)
		salesTotal = 0		
	oldKey = thisKey
	day=thisDay	
	salesTotal += float (thisSale)	
if oldKey != None:
	print oldKey,"\t",day,"\t", salesTotal


