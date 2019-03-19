#!/usr/bin/env python
# -*- coding: latin-1 -*-
'''
Check Missing Image Files.
(c) Benan Cetin
19.03.2019
'''
import mysql.connector
import os
linkbase = 'images/'
fulldir = ''
check = 0
mydb = mysql.connector.connect(
  host="localhost",
  user="xx",
  passwd="xx",
  database="xx"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT imageName FROM imageTable")
myresult = mycursor.fetchall()
for (x,) in myresult:
		if x is not None:
	 		fulldir = linkbase+x
	 		fulldir = fulldir.strip()
	 		print(fulldir)
			if os.path.isfile(fulldir):
				print("File exist :"+fulldir)
			else:
				print("File does not exist :"+fulldir)