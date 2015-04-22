import urllib2
import json
import re,datetime
import sys

list_users = []

def secs(d0):
	d = datetime.datetime(*map(int, re.split('[^\d]', d0)[:-1]))
	epoch = datetime.datetime.utcfromtimestamp(0)
	delta = d - epoch
	return delta.total_seconds()

# Getting the details of all the issues
def get_issue_details(repository, issue_output_file, milestone_output_file):
	miles = set()
	with open(issue_output_file, 'w') as file:
		file.writelines("Issue Number" + "," + "Username" + "," + "Labels" + "," + "State" + "," + "Assignee" + "," + "Milestone" + "," + "Created At" + "," + "Closed At" + "," + "Created-Closed Time Difference(Days)" + '\n')
		f = open(milestone_output_file, "w")
		f.write("Number" + "," + "Title" + "," + "Open issues" + "," + "Closed issues" + "," + "State" + "," + "Created At" + "," + "Due on" + "," + "Closed At" + "\n")
		states = ['open', 'closed']
		
		token = "ee76ae77a8c21b9d7e9eaebcb9e7836ad512e709"
		repo = 'https://api.github.com/repos/' + repository + '/issues'
		page = 1
		while(True):
			for state in states:
				api = repo + '?state=' + state + '&page=' + str(page)
				request = urllib2.Request(api, headers={"Authorization" : "token "+token})
				v = urllib2.urlopen(request).read()
				w = json.loads(v)
				if w:
					for issue in w:
						issue_details = []
						number = issue['number']
						#title = issue['title']
						user_record = issue['user']
						if user_record: user = user_record['login']
						# Anonymizing users
						if user not in list_users:
							list_users.append(user)
						#Changing names of the users
						username = "user" + str(list_users.index(user) + 1)
						
						labels = issue['labels']
						#names = []
						label_names = ""
						if len(labels) > 0:
							for label in labels:
								name = label['name']
								label_names = label_names + name + "|"
						state = issue['state']
						assignee_name = "none"
						assignee_record = issue['assignee']
						if assignee_record:
							assignee = assignee_record['login']
							if assignee not in list_users:
								list_users.append(assignee)
							#Changing names of the users
							assignee_name = "user" + str(list_users.index(assignee) + 1)
						milestone = issue['milestone']
						if milestone: milestone_tag = milestone['title']
						else: milestone_tag = "none"
						created_at = secs(issue['created_at'])
						if issue['closed_at']: closed_at = secs(issue['closed_at'])
						else: closed_at ="none"
						#time difference between created and closed times
						if issue['created_at'] and issue['closed_at']:
							time_diff =((closed_at - created_at)/(3600 * 24))
						else:
							time_diff = "invalid"
						file.writelines(str(number) + ',' + username + ',' + label_names + ',' + state + ',' + assignee_name + ',' + milestone_tag + ',' + str(created_at) + ',' + str(closed_at) + ',' + str(time_diff) + '\n')
						
						# Details for milestones per issue:
						if milestone:
							milestone_number = str(milestone['number'])
							if milestone_number not in miles:
								miles.add(milestone_number)
								milestone_title = milestone['title']
								open_issues = str(milestone['open_issues'])
								closed_issues = str(milestone['closed_issues'])
								milestone_state = milestone['state']
								milestone_create_at = secs(milestone['created_at'])
								milestone_due_on = secs(milestone['due_on'])
								if milestone['closed_at']: milestone_closed_at = secs(milestone['closed_at'])
								else: milestone_closed_at = ""
								f.write(milestone_number + "," + milestone_title + "," + open_issues + "," + closed_issues + "," + milestone_state + "," + str(milestone_create_at) + "," + str(milestone_due_on) + "," + str(milestone_closed_at) + "\n")
						
			page += 1
			if not w : break
		f.close()
	file.close()

# Checking validations of the command line arguments
if len(sys.argv) < 4:
	print "Incorrect number of arguments"
	print "USAGE : python script repository issues_output_file milestone_output_file"
	# Exit if the usage is incorrect
	sys.exit(2)
else:
	repository = sys.argv[1]
	issue_output_file = sys.argv[2]
	milestone_output_file = sys.argv[3]
	get_issue_details(repository, issue_output_file, milestone_output_file)
	