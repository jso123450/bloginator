import sqlite3
import csv

conn = sqlite.connect("blog.db")
c = conn.cursor()

BASE='INSERT INTO users VALUES(%("Username")s,%(UserID)s,%(id)s)'
for l in csv.DictReader(open("users.csv")):
    q=BASE%l
    c.execute(q)

BASE="""
INSERT INTO blogs Value(%("title")s,%("content")s,%(BlogID)s,%(UserID)s)
"""
for l in csv.DictReader(open("blogs.csv")):
    q=BASE%l    
    c.execute(q)

BASE="""
INSERT INTO comments Value(%("content")s.%(CommentID)s,%(BlogID)s,%(UserID)s)
"""
for l in csv.DictReader(open("comments.csv")):
    q=BASE%l
    c.execute(q)

conn.commit
