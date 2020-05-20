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
