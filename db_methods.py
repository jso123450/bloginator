import sqlite3
import pymongo
from pymongo import MongoClient

#File for database methods (registering users, checking if users exist, etc.)

connection = MongoClient()
db = connection['database']
#collections: people, posts, comments

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

def checkUserMongo(username, password):
    person = db.people.find({'un':username},{"pw":password})
    for i in person:
        return True
    return False

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
    
def countUsersMongo():
    people = db.people.find()
    numUsers = 0
    for i in people:
        numUsers+= 1
    return numUsers

def addUser(username, password):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "INSERT INTO users VALUES('" + username + "','" + password + "'," + str(countUsers()) + ");"
    c.execute(q)
    conn.commit()
    conn.close()

def addUserMongo(username, password):
    person = {'un':username,'pw':password,'id':str(countUsersMongo()+1)}
    db.people.insert(person)

def userExists(username):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT Username FROM users;"
    ans = 0
    for i in c.execute(q):
        if i[0] == username:
            ans = True
    if ans != True:
        ans = False
    conn.commit()
    conn.close()
    return ans

def userExistsMongo(username):
    person = db.people.find({'un':username})
    #check if person is empty ?
    for i in person:
        return True
    return False
    
def countPosts():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT BlogID FROM blogs;"
    numBlogs = 0
    for i in c.execute(q):
        numBlogs += 1
    conn.commit()
    conn.close()
    return numBlogs

def countPostsMongo():
    posts = db.posts.find()
    numPosts = 0
    for i in posts:
        numPosts+= 1
    return numPosts

def getUserID(username):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT Username,UserID FROM users;"
    UserID = -1
    for i in c.execute(q):
        if i[0] == username:
            UserID = i[1]
    conn.commit()
    conn.close()
    return UserID

def getUserIDMongo(username):
    person = db.people.find({'un':username})
    return person['id']

def getUsername(ID):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT * FROM users;"
    name = ""
    for i in c.execute(q):
        if i[2] == ID:
            name = i[0]
    conn.commit()
    conn.close()
    return name

def getUsernameMongo(ID):
    person = db.people.find({'id':ID})
    return person['un']

def addPost(title, post, user):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "INSERT INTO blogs VALUES('" + title + "','" + post + "'," + str(countPosts()) + "," + str(getUserID(user)) + ");"
    c.execute(q)
    conn.commit()
    conn.close()

def addPostMongo(title,post,user):
    db.posts.insert({'title':title,'content':post,'blogid':str(countPostsMongo()+1),'userid':getUserIDMongo(user)})

def editPost(content, BlogID):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "UPDATE blogs SET Content='" + content + "' WHERE BlogID=" + BlogID + ";"
    c.execute(q)
    conn.commit()
    conn.close()

def editPostMongo(content,BlogID):
    post = db.posts.find({'blogid':BlogID})
    title = post['title']
    userid = post['userid']
    db.posts.update({'postid':BlogID},{'title':title,'content':content,'blogid':BlogID,'userid':userid})

def editUserPost(content, BlogID, username):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    UserID = getUserID(username)
    q = "SELECT BlogID,UserID FROM blogs;"
    counter1 = -1
    counter2 = -1
    for i in c.execute(q):
        counter2 += 1
        if i[1] == UserID:
            counter1 += 1
            if counter1 == int(BlogID):
                conn.commit()
                conn.close()
                editPost(content, str(counter2))
                break

# def editUserPostMongo(content, BlogID, username):
#     post = db.posts.find({'blogid':BlogID})
#     title = post['title']
#     userid = post['userid']
#     db.posts.update(
def getPosts():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    blogList = [] #A list of lists (smaller lists have title and content of one blog post)
    q = "SELECT Title,Content,UserID FROM blogs;"
    for i in c.execute(q):
        username = getUsername(i[2])
        blog = [i[0], i[1], username] #A list with the title and content
        blogList.append(blog)
    conn.commit()
    conn.close()
    return blogList

def getPostsMongo():
    blogList = []
    posts = db.posts.find()
    for i in posts:
        username = getUsernameMongo(i['userid'])
        blog = [i['title'],i['content'],username]
        blogList.append(blog)
    return blogList

def getUserPosts(username):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    blogList = []
    q = "SELECT Title,Content,UserID FROM blogs;"
    for i in c.execute(q):
        dbUsername = getUsername(i[2])
        if username == dbUsername:
            blog = [i[0], i[1]]
            blogList.append(blog)
    conn.commit()
    conn.close()
    return blogList

def getUserPostsMongo(username):
    blogList = []
    posts = db.posts.find({'un':username})
    for i in posts:
        blogList.append(i)
    return blogList
