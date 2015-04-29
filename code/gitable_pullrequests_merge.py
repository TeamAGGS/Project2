
import urllib2
import json
import re,datetime
import sys

list_users = []
a = []
	

def secs(d0):
	d = datetime.datetime(*map(int, re.split('[^\d]', d0)[:-1]))
	epoch = datetime.datetime.utcfromtimestamp(0)
	delta = d - epoch
	return delta.total_seconds()

# Getting the details of all the pull requests
def get_pull_details(repository, pullrequests_output_file):	
	f = open(pullrequests_output_file, "w")
	f.write("Id" + "," + "Number" + "," + "State" + "," + "Created At" + "," + "Closed At" + "," + "Merged At" + "," + "Created-Closed Time Difference(Days)" + "," + "Username" + "," + "Merged By" + '\n')
	token = "<Insert token here>"
	repo = 'https://api.github.com/repos/' + repository + '/pulls'
	page = 1
	while(True):
		
		api = repo + '?state=' + 'all' + '&page=' + str(page)
		request = urllib2.Request(api, headers={"Authorization" : "token "+token})
		v = urllib2.urlopen(request).read()
		w = json.loads(v)
		if w:
			for req in w:
				number = req['number']
				a.append(number)
		page += 1
		
		if not w : break
	
	for num in a:
		repo = 'https://api.github.com/repos/' + repository + '/pulls/' + str(num)
		#api = repo + '?state=' + 'all' + '&page=' + str(page)
		request = urllib2.Request(repo, headers={"Authorization" : "token "+token})
		v = urllib2.urlopen(request).read()
		req = json.loads(v)
		if req:
			#if req.has_key('pull_request'):
			id = req['id']
			number = req['number']
			#title = req['title']
			state = req['state']
			if req['created_at']: 
				created_at = (req['created_at'])
				created_at_sec = secs(req['created_at'])
			if req['closed_at']: 
				closed_at_sec = secs(req['closed_at'])
				closed_at = (req['closed_at'])
			if req['merged_at']: merged_at = (req['merged_at'])
			if req['merged_by']: merged_by = (req['merged_by']['login'])
			if merged_by not in list_users:
				list_users.append(merged_by)
			merged_by = "user" + str(list_users.index(merged_by) + 1)
			#time difference between created and closed times
			if req['created_at'] and req['closed_at']:
				time_diff =((closed_at_sec - created_at_sec)/(60))
			else:
				time_diff = "invalid"
			user_record = req['user']
			if user_record: user = user_record['login']
			# Anonymizing users
			if user not in list_users:
				list_users.append(user)
			#Changing names of the users
			username = "user" + str(list_users.index(user) + 1)
			f.write(str(id) + "," + str(number) + "," + state + "," + str(created_at) + "," + str(closed_at) + "," + str(merged_at) + "," + str(time_diff) + "," + username + "," + str(merged_by) + '\n')
	page += 1
		
	
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
	
