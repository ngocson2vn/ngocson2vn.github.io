#!/usr/bin/python

import glob
import sys
import os
import eyed3

if len(sys.argv) < 4:
	print "python %s <rename | edit> <n>" % sys.argv[0]
	sys.exit(0)

p = sys.argv[1]
mode = sys.argv[2]
n = int(sys.argv[3])
print p, mode

filelist = glob.glob(p + "*.mp3")

if mode == "rename":
	i = n
	for f in filelist:
		d, fn = os.path.split(f)
		os.rename(f, p + "Track%03d.mp3" % (i))
		print fn + " --> " + "Track%03d.mp3" % (i)
		i = i + 1
elif mode == "edit":
	i = 1
	for f in filelist:
		print f
		audiofile = eyed3.load(f)
		audiofile.tag.artist = u"Soumatome"
		audiofile.tag.album_artist = u"Soumatome"
		audiofile.tag.album = u"SoumatomeChoukaiN2"
		audiofile.tag.title = u"Track%03d" % i
		audiofile.tag.track_num = i

		audiofile.tag.save()
		i = i + 1

