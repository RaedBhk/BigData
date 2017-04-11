#!/usr/bin/python
import sys
import string

for line in sys.stdin:	
	post_id = "-"
	title = "-"
	tagnames = "-"
	author_id = "-"
	node_type = "-"
	parent_id = "-" 
	abs_parent_id = "-"
	added_at = "-"
	score = "-"
	reputation = "-"
	gold = "-"
	silver = "-" 
	bronze = "-"
	data = line.strip().split("\t")
	if len(data) == 5:
		author_id = data[0]		
		reputation = data[1]
		gold = data[2]
		silver = data[3] 
		bronze = data[4]
		print "{0}\t{1}\t{2}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(author_id,post_id ,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,silver,bronze)	
		
	if len(data) == 19:
		post_id = data[0]
		title = data[1]
		tagnames = data[2] 
		author_id = data[3]
		node_type = data[5]
		parent_id = data[6] 
		abs_parent_id = data[7]
		added_at = data[8]
		score = data[9]
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(author_id,post_id ,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,silver,bronze)	
		
	

		
				
		

