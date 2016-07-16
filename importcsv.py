#!/usr/bin/python

import sys
import sqlite3
import subprocess

#if len(sys.argv) < 4:
#	print "python %s <data file> <table> <dry mode>" % sys.argv[0]
#	sys.exit(0)

db = "jpvocab.db"
dbInfo = "info.db"
csv = "leveln2.txt"
table = "leveln2"
dry = "0"
startIdx = 0

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
		
		if (not data[0] or not data[2]):
			print data[0], data[1], data[2]
			print "line:", lineCount
			sys.exit(0)

		if data[1] == '':
			data[1] = data[0]

		if len(data) == 3:
			data.append("")

		cmd = "insert into leveln2 values (NULL, '%s', '%s', '%s', '%s', '%s', 0)" % (data[0], data[1], "NO", data[2], data[3])
		print "%d: %s" % (lineCount, cmd)
		try:
			c.execute(cmd)
		except:
			cmd = "update leveln2 set hiragana='%s', vn='%s', ex='%s' where kanji='%s'" % (data[1], data[2], data[3], data[0])
			c.execute(cmd)
		line = f.readline()
		line = line[:-2]
		lineCount = lineCount + 1

	totalWord = 0
	for row in c.execute("SELECT COUNT(id) FROM leveln2"):
		totalWord = row[0]
		print totalWord

	if dry == "0":
		conn.commit()
		fileSize = subprocess.Popen("du -hs jpvocab.db", shell=True, stdout=subprocess.PIPE).stdout.read().split()[0]
		print fileSize

		info.execute("UPDATE info SET leveln2=%d, min_n2=1, max_n2=%d, size='%s'" % (totalWord, totalWord, fileSize))
		connObj.commit()

		print subprocess.Popen("git commit -a -m 'Update'; git push", shell=True, stdout=subprocess.PIPE).stdout.read()

def import_vocab_n2():
	f = open(csv)

	line = f.readline()
	line = line[:-2]
	startIdx = int(line)

	line = f.readline()
	line = line[:-2]

	conn = sqlite3.connect(db)
	c = conn.cursor()

	connObj = sqlite3.connect(dbInfo)
	info = connObj.cursor()

	lineCount = 1
	idx = startIdx
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
		if data[3] == '-':
			data[3] = ' '

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

		info.execute("UPDATE info SET total_n2=%d, size='%s', min_n2=%d, max_n2=%d" % (totalWord, fileSize, startIdx, (idx - 1)))
		connObj.commit()

		print subprocess.Popen("git commit -a -m 'Update'; git push", shell=True, stdout=subprocess.PIPE).stdout.read()

import_csv()
#if table == "leveln2":
#	import_csv()
#else:
#	import_vocab_n2()
