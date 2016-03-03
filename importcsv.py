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

	lineCount = 1
	while line:
		data = []
		for x in line.split("#"):
			data.append(x)
		
		if (not data[0] or not data[1] or not data[2] or not data[3]):
			print data[0], data[1], data[2], data[3]
			print "line:", lineCount
			sys.exit(0)

		if data[1] == '-':
			data[1] = ' '

		cmd = "insert into vocab values (NULL, '%s', '%s', '%s', '%s')" % (data[0], data[1], data[2], data[3])
		print "%d: %s" % (lineCount, cmd)
		c.execute(cmd)
		line = f.readline()
		line = line[:-2]
		lineCount = lineCount + 1

	totalWord = 0
	for row in c.execute("SELECT COUNT(id) FROM vocab"):
		totalWord = row[0]
		print totalWord

	if dry == "0":
		conn.commit()
		fileSize = subprocess.Popen("du -hs jpvocab.db", shell=True, stdout=subprocess.PIPE).stdout.read().split()[0]
		print fileSize

		info.execute("UPDATE info SET total=%d, size='%s'" % (totalWord, fileSize))
		connObj.commit()

		print subprocess.Popen("git commit -a -m 'Update'; git push", shell=True, stdout=subprocess.PIPE).stdout.read()

def import_vocab_n2():
	f = open(csv)

	line = f.readline()
	line = line[:-2]

	conn = sqlite3.connect(db)
	c = conn.cursor()

	connObj = sqlite3.connect(dbInfo)
	info = connObj.cursor()

	lineCount = 1
	idx = 511
	while line:
		data = []
		for x in line.split("#"):
			data.append(x)
		
		if (not data[0] or not data[1] or not data[2] or not data[3]):
			print data[0], data[1], data[2], data[3]
			print "line:", lineCount
			sys.exit(0)

		if data[1] == '-':
			data[1] = ' '

		cmd = "insert into vocab_n2 values (%d, '%s', '%s', '%s', '%s')" % (idx, data[0], data[1], data[2], data[3])
		print "%d: %s" % (lineCount, cmd)
		c.execute(cmd)
		line = f.readline()
		line = line[:-2]
		lineCount = lineCount + 1
		idx = idx + 1

	totalWord = 0
	for row in c.execute("SELECT COUNT(id) FROM vocab_n2"):
		totalWord = row[0]
		print totalWord

	if dry == "0":
		conn.commit()
		fileSize = subprocess.Popen("du -hs jpvocab.db", shell=True, stdout=subprocess.PIPE).stdout.read().split()[0]
		print fileSize

		info.execute("UPDATE info SET total_n2=%d, size='%s'" % (totalWord, fileSize))
		connObj.commit()

		print subprocess.Popen("git commit -a -m 'Update'; git push", shell=True, stdout=subprocess.PIPE).stdout.read()
#import_csv()

import_vocab_n2()
