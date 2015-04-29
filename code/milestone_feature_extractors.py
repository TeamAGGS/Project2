import sys
import csv
import numpy
#script to use raw data and create some interesting feature extractors for milestones data

def median(lst):
    return numpy.median(numpy.array(lst))

def add_feature_extractors(input_file, output_file):
	f = open(output_file, "w")
	v = open(input_file, "r")
	r = csv.reader(v)
	w = csv.writer(f, lineterminator='\n')

	all = []
	row = r.next()
	row.append('Number of Times Milestone Used')
	row.append('Time Difference Created and Closed')
	row.append('Time Difference Due on and Closed')
	all.append(row)
	open_issues = 0
	total_issues = {}
	total = []

	for row in r:
		# Adding open issues
		open_issues = open_issues + int(row[2])
		# Adding the total issues column
		issues = (int(row[2]) + int(row[3]))
		row.append(str(issues))
		total_issues[(row[0])] = issues
		total.append(issues)
		# Time between creating and closing times
		if(row[7] != ""):
			time_diff =((float(row[7]) - float(row[5]))/(3600 * 24))
			time_due =((float(row[7]) - float(row[6]))/(3600 * 24))
		else:
			time_diff = ""
			time_due = ""
		row.append(str(time_diff))
		# Time between due on and closing times
		row.append(str(time_due))

		all.append(row)
	w.writerows(all)
	# Checking is any issues are still open
	if(open_issues > 0 ):
		print("Alert : There are issues still open")
	
	# Checking is unusual small number of issues or unusual large number of issues
	med = median(total)
	for num, issues in total_issues.iteritems():
		if issues < med/2:
			print("Unusually small number of issues detected for milestone number : " + str(num))
		elif issues > med*2:
			print("Unusually large number of issues detected for milestone number : " + str(num))
	
# Checking validations of the command line arguments
if len(sys.argv) < 3:
	print "Incorrect number of arguments"
	print "USAGE : python script team_milestone_file output_file "
	# Exit if the usage is incorrect
	sys.exit(2)
else:
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	add_feature_extractors(input_file, output_file)