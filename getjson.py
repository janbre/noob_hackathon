#!/bin/python

#imports 
import os

#input file
fname = "urls"

#read all the lines in the url file.
with open(fname) as f:
    content = f.readlines()

# for all urls wget the json file. 
for link in content:
	pre = "wget -O "
	dest = "./fag/" + link.strip().split("/")[-1] + " "
	getfile = link.strip()
	#print pre + dest + getfile
	#wget -O ./fag/SOK8617 www.ime.ntnu.no/api/course/SOK8617
	os.system(pre + dest + getfile)
