#!/usr/bin/python

import sys
import shutil
import re

input_file = sys.argv[1]

f = open(input_file)
fw = open(input_file + '.fixed', 'w')

i = 1
line = f.readline()

while line:
	words = line.split("#")
	
	if len(words[1]) < len(words[0]) and words[1] != '-':
		print "=>line %d: %s" % (i, words[0])
	elif words[0] == words[1]:
		print "==>line %d: %s" % (i, words[0])
		words[1] = '-'
	else:
		lw = len(words[0].decode('utf8'))
		k = 0
		for uc in words[0].decode('utf8'):
			if not re.search(u'[\u4e00-\u9faf]', uc):
				k = k + 1
		if k == lw and words[1] != '-':
			print "===>line %d: %s" % (i, words[0])
			words[1] = '-'

	fw.write("%s#%s#%s#%s" % (words[0], words[1], words[2], words[3]))
	
	i = i + 1
	line = f.readline()

f.close()
fw.close()
shutil.move(input_file, 'backup')
