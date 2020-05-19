# import base64
# import json
# import os
# import re
# import requests


# def removeComments(prgm):
# 	n = len(prgm)
# 	#print(n)
# 	res = ""
# 	s_cmt = False
# 	m_cmt = False
# 	#Traverse the given program 
# 	i = 0
# 	while(i<n):
# 		#print(prgm[i])
# 		if(s_cmt == True and prgm[i] == '\n'):
# 			s_cmt = False
# 		elif(m_cmt == True and prgm[i] == '*' and prgm[i+1] == '/'):
# 			m_cmt = False 
# 			i = i + 1
# 		elif(s_cmt or m_cmt):
# 			i = i + 1
# 			continue; 
# 		elif(prgm[i] == '/' and prgm[i+1] == '/'): 
# 			s_cmt = True
# 			i = i + 1
# 		elif(prgm[i] == '/' and prgm[i+1] == '*'):
# 			m_cmt = True
# 			i = i + 1 
# 		else:
# 			#print(res+"hi")
# 			res = res + prgm[i]
# 		i = i + 1
# 	return res


# def create_comment(comment,username,repo,pr_number):
# 	repo = repo
# 	pr_number = pr_number
# 	username = username
# 	url = "https://api.github.com/repos/"+username+"/"+repo+"/pulls/"+pr_number
# 	r = requests.get(url)
# 	r_json = r.json()
# 	another_url = r_json['_links']['comments']['href']
# 	headers={
#         'Content-Type': "application/json",
#         'Authorization': "Basic dmluZWV0aHZlbGlnZXRpOnZpbm55YnVubnkxMjM=",
#     }
# 	payload={"side": "LEFT","body":comment}
# 	response = requests.request("POST", another_url, data=json.dumps(payload), headers=headers)
# 	#print(response.text)
# def handle_pr():
# 	if 'payload' not in os.environ:
# 		print('scm payload needs to be present like Github  or Bit_bucket')
# 		return
# 	payload = os.environ['payload']
# 	payload_json = json.loads(payload)
# 	pr_number = str(payload_json['number'])
# 	repo = payload_json['repository']['name']
# 	username = payload_json['repository']['owner']['login']
# 	# pr_number = "4"
# 	# repo = "Hello-world"
# 	# username = "Thati0103"
# 	#Query to get the number of files changed
# 	url = 'https://api.github.com/repos/'+username+'/'+repo+'/pulls/'+pr_number+'/files'
# 	r = requests.get(url)
# 	changes_json = r.json()
# 	#print(changes_json)
# 	length = len(changes_json)
# 	no_of_files = length
# 	#Checking if rule1 satisfies
# 	if no_of_files > 10:
# 		#print("Warning:Commit another PR")
# 		create_comment("###### Warning: Commit another PR (Number of files > 10)",username,repo,pr_number)
# 	#Query to get pull request description
# 	url = 'https://api.github.com/repos/'+username+'/'+repo+'/pulls/'+pr_number
# 	r_new = requests.get(url)
# 	print(r_new.json())
# 	if r_new.json()['body'] == "":
# 		create_comment("###### Warning: Add description ",username,repo,pr_number)
# 	else:
# 		create_comment("Description is added ",username,repo,pr_number)
# 	#Query to check if Lines of code in files is greater than 1000
# 	i = 0
# 	for i in range(length):
# 		file_name = changes_json[i]['filename']
# 		url_new = changes_json[i]['contents_url']
# 		new_req = requests.get(url_new)
# 		file_json = new_req.json()
# 		content = base64.b64decode(file_json['content'])
# 		message = content.decode('utf-8')
# 		Loc = message.count('\n')
# 		if(Loc > 1000):
# 			#print("Warning:Lines of code in file "+file_name+"exceeded 1000")
# 			create_comment("###### Warning: Lines of code in file "+file_name+" exceeded 1000",username,repo,pr_number)
# 	#Query to check if test folder is changed or not
# 	sourcecode_files = 0
# 	testcode_files = 0
# 	i = 0
# 	for i in range(length):
# 		file_name = changes_json[i]['filename']
# 		length_1 = len(file_name)
# 		index_source = file_name.find('src',0,length_1-1)
# 		index_test = file_name.find('test',0,length_1-1)
# 		if(index_source != -1):
# 			sourcecode_files = sourcecode_files + 1
# 		if(index_test != -1):
# 			testcode_files = testcode_files + 1
# 	if(sourcecode_files > 0):
# 		if(testcode_files <= 0):
# 			#print("Warning:Tests are not added")
# 			create_comment("###### Warning: Tests are not added",username,repo,pr_number)
# 	#Query to check if code is commented one or not
# 	for i in range(0,length):
# 		file_name = changes_json[i]['filename']
# 		url_new = changes_json[i]['contents_url']
# 		b_in_dict = "patch" in changes_json[i]
# 		if(b_in_dict):
# 			patch = changes_json[i]['patch']
# 			codes = []
# 			codes = patch.split('\n')
# 			length = len(codes)
# 			for i in range(length):
# 				if(codes[i][0] == "+"):
# 					index = i
# 					break
# 			str_1 = ""
# 			for i in range(index,length):
# 				leng = len(codes[i])
# 				for j in range(0,leng-1):
# 					str_1 = str_1 + codes[i][j+1]
# 				str_1 = str_1 + '\n'
# 			#print(str_1)
# 			new_s = removeComments(str_1)
# 			new_str_1 = new_s.replace("\n","")
# 			#print(new_str_1)
# 			if(new_str_1 == ""):
# 				create_comment("Warning:Code committed is commented one.Please check again!!",username,repo,pr_number)
		
# # handle_pr()
