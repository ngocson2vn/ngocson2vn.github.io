#!/usr/bin/python

import sys
import sqlite3

conn = sqlite3.connect("jpvocab.db")
c = conn.cursor()
#c.execute("DROP TABLE vocab")
#c.execute("CREATE TABLE vocab(id integer primary key, kanji text UNIQUE NOT NULL, hiragana text NOT NULL, en text NOT NULL, vn text NOT NULL)")
c.execute("DROP TABLE leveln2")
c.execute("CREATE TABLE leveln2(id integer primary key, kanji text UNIQUE NOT NULL, hiragana text NOT NULL, en text NOT NULL, vn text NOT NULL, ex text)")
conn.commit()
