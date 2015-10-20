#!/usr/bin/python

import sys
import sqlite3
import subprocess

db = "jpvocab.db"
dbInfo = "info.db"
csv = sys.argv[1]
dry = sys.argv[2]

def import_csv():
	f = open(csv)

	line = f.readline()
	line = line[:-2]

	conn = sqlite3.connect(db)
	c = conn.cursor()

	connObj = sqlite3.connect(dbInfo)
	info = connObj.cursor()

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

	totalWord = 0
	for row in c.execute("SELECT COUNT(id) FROM vocab"):
		totalWord = row[0]
		print totalWord

	if dry == "0":
		conn.commit()
		fileSize = subprocess.Popen("du -hs jpvocab.db", shell=True, stdout=subprocess.PIPE).stdout.read().split()[0]
		print fileSize

		info.execute("UPDATE info SET total=%d, size='%s'" % (totalWord, fileSize))

		print subprocess.Popen("git commit -a -m 'Update'; git push", shell=True, stdout=subprocess.PIPE).stdout.read()


import_csv()
