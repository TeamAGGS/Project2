import sys
import csv
import numpy
# script for bad smells detector using feature extractors for milestones data

def median(lst):
    return numpy.median(numpy.array(lst))
	
def detect_bad_smells(input_file):
	v = open(input_file, "r")
	per_row = []
	for line in v:
		per_row.append(line.split(','))
	per_column = zip(*per_row)
	
	#Checking if milestone closed on due date or late by due date
	print("Milestones closed past due date : \n")
	for time in per_column[10][1:]:
		if(time != "" and float(time) > 1.0):
			index = (per_column[10].index(time))
			print("Milestone : " + str(per_column[0][index]))
	#Checking if unusual small number of issues in milestones but great time spent on items
	print("Milestones tags with unusual small number of issues but excess time spent on them")
	#Find median time spent on each milestone
	times = []
	for time_spent in per_column[9][1:]:
		if(time_spent != ""):
			times.append(float(time_spent))
	med_time = median(times)
	for i,x in enumerate(per_column[11]):
		if x.lower() == 'yes':
			#check if time spent is greater than median
			time = per_column[9][i]
			if(float(time) > med_time):
				print("Milestone : " + str(per_column[0][i]) + "\n")
	#Checking if unusual large number of issues in milestones but less time spent
	print("Milestones tags with unusual large number of issues but very limited time spent on them")
	
	for j,y in enumerate(per_column[12]):
		if('yes' in y):
			#check if time spent is lower than median
			time1 = per_column[9][j]
			if(float(time1) < med_time):
				print("Milestone : " + str(per_column[0][j]) + "\n")

	#Checking is the number of times each milestones was used is not evenly spread - shows tasks are divided and initial planning for milestones is not done appropriately
	
# Checking validations of the command line arguments
if len(sys.argv) < 2:
	print "Incorrect number of arguments"
	print "USAGE : python script milestone_features_file "
	# Exit if the usage is incorrect
	sys.exit(2)
else:
	input_file = sys.argv[1]
	detect_bad_smells(input_file)