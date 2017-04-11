#!/usr/bin/python
import sys
salesTotal=0
salesNum=0
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 3:
		continue

	thisKey, thisSalesTotal,thisSalesNum = data
	salesTotal += float(thisSalesTotal)
	salesNum += int(thisSalesNum)

print thisKey,"\t",salesNum,"\t",salesTotal


