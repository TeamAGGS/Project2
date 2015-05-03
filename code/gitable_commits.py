

import urllib2
import json
import re,datetime
import sys

list_users = []
count = 0

# Getting the details of all the pull requests
def get_pull_details(repository, pullrequests_output_file):	
	f = open(pullrequests_output_file, "w")
	f.write("Commit sha" + "," + "Name" + "," + "date" + '\n')
	token = "b0ab70c3e4a368883d418a4cd8e1550803708830"
	repo = 'https://api.github.com/repos/' + repository + '/commits'
	page = 1
	while(True):
		api = repo + '?' + '&page=' + str(page)
		request = urllib2.Request(api, headers={"Authorization" : "token "+token})
		v = urllib2.urlopen(request).read()
		w = json.loads(v)
		if w: 
			for req in w:
				sha = req['sha']
				
				if (req['committer'] == None): user_record = 'Unknown'
				else : user_record = req['committer']['login']
				date = req['commit']['committer']['date']
				
				# Anonymizing users
				if user_record not in list_users:
					list_users.append(user_record)
				#Changing names of the users
				username = "user" + str(list_users.index(user_record) + 1)
				f.write(str(sha) + "," + str(username) + "," + str(date) + '\n')	
		page += 1
		
		if not w : break
	
	f.close()

# Checking validations of the command line arguments
if len(sys.argv) < 3:
	print ("Incorrect number of arguments")
	print ("USAGE : python script repository pullrequests_output_file ")
	# Exit if the usage is incorrect
	sys.exit(2)
else:
	repository = sys.argv[1]
	pullrequests_output_file = sys.argv[2]
	get_pull_details(repository, pullrequests_output_file)
	
