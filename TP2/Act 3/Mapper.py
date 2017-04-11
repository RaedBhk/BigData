#!/usr/bin/python
import sys
from datetime import datetime
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		weekday = datetime.strptime(date,"%Y-%m-%d").weekday()
		if(weekday==0):
			print "{0}\tSunday\t{1}".format(weekday,cost)
		if(weekday==1):
			print "{0}\tMonday\t{1}".format(weekday,cost)
		if(weekday==2):
			print "{0}\tTuesday\t{1}".format(weekday,cost)
		if(weekday==3):
			print "{0}\tWednesday\t{1}".format(weekday,cost)
		if(weekday==4):
			print "{0}\tThursday\t{1}".format(weekday,cost)
		if(weekday==5):
			print "{0}\tFriday\t{1}".format(weekday,cost)
		if(weekday==6):
			print "{0}\tSaturday\t{1}".format(weekday,cost)

