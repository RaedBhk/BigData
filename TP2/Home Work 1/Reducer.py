#!/usr/bin/python
import sys
import string

last_auth_id = None
cur_reputation = "-"
cur_gold = "-"
cur_silver = "-"
cur_bronze = "-"

for line in sys.stdin:
	data = line.strip().split("\t")
	auth_id = data[0]
	post_id = data[1]
	title = data[2]
	tagnames = data[3] 	
	node_type = data[4]
	parent_id = data[5] 
	abs_parent_id = data[6]
	added_at = data[7]
	score = data[8]
	reputation = data[9]
	gold = data[10]
	silver = data[11] 
	bronze = data[12]
	
		
	if not last_auth_id or last_auth_id != auth_id:
		last_auth_id = auth_id
		cur_reputation = reputation
		cur_gold = gold
		cur_silver = silver
		cur_bronze = bronze
	elif auth_id == last_auth_id:					
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(post_id ,title,auth_id,tagnames,node_type,parent_id,abs_parent_id,added_at,score,cur_reputation,cur_gold,cur_silver,cur_bronze)	
		
        			
		
