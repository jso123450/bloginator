import sqlite3

#File for database methods (registering users, checking if users exist, etc.)

def checkUser(username, password):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT * FROM users;"
    for i in c.execute(q):
        print i
    q = "SELECT Username,Password FROM users;"
    for i in c.execute(q):
        if i[0] == username and i[1] == password:
            return True
    return False
    conn.commit()
    conn.close()

def countUsers():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT UserID FROM users;"
    numUsers = 0
    for i in c.execute(q):
        numUsers += 1
    conn.commit()
    conn.close()
    return numUsers
    
def addUser(username, password):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    alreadyExists = False
    q = "SELECT Username FROM users;"
    for i in c.execute(q):
        if i[0] == username:
            alreadyExists = True
    if not alreadyExists:
        q = "INSERT INTO users VALUES('" + username + "','" + password + "'," + str(countUsers()) + ");"
        c.execute(q)
    conn.commit()
    conn.close()

def countPosts():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT BlogID FROM blogs"
    numBlogs = 0
    for i in c.execute(q):
        numBlogs += 1
    conn.commit()
    conn.close()
    return numBlogs

def getID(username):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT * FROM users"
    UserID = -1
    for i in c.execute(q):
        if i[0] == username:
            UserID = i[2]
    conn.commit()
    conn.close()
    return UserID

def addPost(title, post, user):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "INSERT INTO blogs VALUES('" + title + "','" + post + "'," + str(countPosts()) + "," + str(getID(user)) + ");"
    c.execute(q)
    conn.commit()
    conn.close()

def getPosts():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    blogList = [] #A list of lists (smaller lists have title and content of one blog post)
    q = "SELECT Title,Content FROM blogs"
    for i in c.execute(q):
        blog = [i[0], i[1]] #A list with the title and content
        blogList.append(blog)
    conn.commit()
    conn.close()
    return blogList
