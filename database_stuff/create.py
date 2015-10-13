import sqlite3

conn = sqlite3.connect("blog.db")

c = conn.cursor()

q = "create table users(Username text, UserID integer)"
c.execute(q)

q = "create table blogs(title text, content text, BlogID integer, UserId integer)"
c.execute(q)

q = "create table comments(content text, CommentID integer, BlogID integer, UserID integer)"
c.execute(q)

conn.commit() 