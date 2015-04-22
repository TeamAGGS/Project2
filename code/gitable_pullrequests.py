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

# Getting the details of all the pull requests
def get_pull_details(repository, pullrequests_output_file):	
	f = open(pullrequests_output_file, "w")
	f.write("Id" + "," + "Number" + "," + "Title" + "," + "State" + "," + "Created At" + "," + "Closed At" + "," + "Created-Closed Time Difference(Days)" + "," + "Merged At" + "," + "Username" + '\n')
	token = "Insert your token here"
	repo = 'https://api.github.com/repos/' + repository + '/pulls'
	page = 1
	while(True):
		api = repo + '?state=' + 'all' + '&page=' + str(page)
		request = urllib2.Request(api, headers={"Authorization" : "token "+token})
		v = urllib2.urlopen(request).read()
		w = json.loads(v)
		if w:
			for req in w:
				id = req['id']
				number = req['number']
				title = req['title']
				state = req['state']
				if req['created_at']: created_at = secs(req['created_at'])
				if req['closed_at']: closed_at = secs(req['closed_at'])
				if req['merged_at']: merged_at = secs(req['merged_at'])
				#time difference between created and closed times
				if req['created_at'] and req['closed_at']:
					time_diff =((closed_at - created_at)/(3600 * 24))
				else:
					time_diff = "invalid"
				user_record = req['user']
				if user_record: user = user_record['login']
				# Anonymizing users
				if user not in list_users:
					list_users.append(user)
				#Changing names of the users
				username = "user" + str(list_users.index(user) + 1)
				f.write(str(id) + "," + str(number) + "," + str(title) + "," + state + "," + str(created_at) + "," + str(closed_at) + "," + str(time_diff) + "," + str(merged_at) + "," + username + '\n')
		page += 1
		if not w : break
	f.close()

# Checking validations of the command line arguments
if len(sys.argv) < 3:
	print "Incorrect number of arguments"
	print "USAGE : python script repository pullrequests_output_file "
	# Exit if the usage is incorrect
	sys.exit(2)
else:
	repository = sys.argv[1]
	pullrequests_output_file = sys.argv[2]
	get_pull_details(repository, pullrequests_output_file)
	
