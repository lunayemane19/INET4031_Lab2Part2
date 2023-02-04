#!/usr/bin/env python3

file = open("fileprocessor.input","r")

data = file.readlines()
data = [x.strip("\n") for x in data]

data_list = [x.split(":") for x in data]
#data_list = [x.strip("\n") for x in data_list]

#print(data_list)

print("Printing out User Data:\n")

for x in data_list:
	if x[0] ==  "#User4":
		break
	else: 
		print("The user %r has a password of %r  and has userid %r and groupid %r ." % (x[0],x[1],x[2],x[3]))


print("User4 is skipped because it starts with a hashtag (is commented out)\n\nEnd of User Data")






