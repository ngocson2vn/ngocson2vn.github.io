#!/usr/bin/python

import sys
import sqlite3

csv = sys.argv[1]
db = sys.argv[2]
dry = sys.argv[3]

def import_csv():
	f = open(csv)

	line = f.readline()
	line = line[:-2]

	conn = sqlite3.connect(db)
	c = conn.cursor()
	while line:
		data = []
		for x in line.split("*"):
			data.append(x)
		#print data
		cmd = "insert into vocab values (NULL, '%s', '%s', '%s', '%s')" % (data[0], data[1], data[2], data[3])
		print cmd
		c.execute(cmd)
		line = f.readline()
		line = line[:-2]

	if dry == "0":
		conn.commit()

import_csv()
