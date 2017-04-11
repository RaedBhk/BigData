#!/usr/bin/python
import sys
Total = 0
oldword = None
idList=""
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	word, node  = data
	if oldword and oldword != word:
		print "{0}\t{1}\t{2}".format(oldword,Total, idList)
		Total = 0
		idList=""
	oldword = word
	Total = Total + 1
	idList= idList + " " + node
if oldword != None:
	print oldword,"\t", Total,"\t", idList
