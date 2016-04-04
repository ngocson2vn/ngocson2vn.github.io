#!/usr/bin/python

import glob
import sys
import os
import eyed3

p = sys.argv[1]
print p

filelist = glob.glob(p + "*.mp3")

#i = 1
#for f in filelist:
#	d, fn = os.path.split(f)
#	os.rename(f, p + "Track%03d.mp3" % (i))
#	print fn + " --> " + "Track%03d.mp3" % (i)
#	i = i + 1

i = 1
for f in filelist:
	print f
	audiofile = eyed3.load(f)
	audiofile.tag.artist = u"Mimi"
	audiofile.tag.album_artist = u"Mimi"
	audiofile.tag.album = u"MimiN2"
	audiofile.tag.title = u"Track%03d" % i
	audiofile.tag.track_num = i

	audiofile.tag.save()
	i = i + 1

