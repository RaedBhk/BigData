#!/usr/bin/python
import sys
import re
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 19:
		
		node=data[0]
		body=data[4]
		words=re.split(r';| |:|!|\?|\.|"|<|>|[|]|\#|\$|=|-|/|\(|\)|,',body)	
		
		for word in words:
			if word != '':
				print "{0}\t{1}".format(word,data[0])
		
		
		

