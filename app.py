from flask import Flask, render_template, request, session, redirect, url_for
import db_methods

app = Flask(__name__)

#This will be the general blog (before logging in)
@app.route("/", methods = ["GET", "POST"])
def blog():
    blogs = db_methods.getPosts()
    if session.has_key("loggedIn") and session["loggedIn"]:
        if request.form.has_key("BlogID"):
            return render_template("blog.html", loggedIn = True, username = session["username"], blogs = blogs, editing = request.form["BlogID"])
        else:
            if request.form.has_key("edit"):
                db_methods.editPost(request.form["edit"], request.form["editedID"])
                blogs = db_methods.getPosts()
            return render_template("blog.html", loggedIn = True, username = session["username"], blogs = blogs, editing = "-1")
    else:
        if request.form.has_key("BlogID"):
            return redirect(url_for("login"))
        else:
            return render_template("blog.html", loggedIn = False, blogs = blogs)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.form.has_key("username") and request.form.has_key("password"):
        if db_methods.checkUser(request.form["username"], request.form["password"]):
            session["loggedIn"] = True
            session["username"] = request.form["username"]
            return redirect(url_for("blog"))
        else:
            return render_template("login.html", error = "Invalid username or password")
    else:
        if session.has_key("loggedIn") and session["loggedIn"]:
            return redirect(url_for("blog"))
        else:
            return render_template("login.html")

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if session.has_key("loggedIn") and session["loggedIn"]:
        return redirect(url_for("blog"))
    else:
        if request.form.has_key("username"):
            if request.form["password"] != request.form["confirmPassword"]:
                return render_template("signup.html", error = "Password does not match confirm password")
            else:
                if not db_methods.userExists(request.form["username"]):
                    db_methods.addUser(request.form["username"], request.form["password"])
                    session["loggedIn"] = True
                    session["username"] = request.form["username"]
                    return redirect(url_for("myposts"))
                else:
                    return render_template("signup.html", error = "Username already exists")
        else:
            return render_template("signup.html")

@app.route("/myposts", methods = ["GET", "POST"])
def myposts():
    if session.has_key("loggedIn") and session["loggedIn"]:
        userPosts = db_methods.getUserPosts(session["username"])
        if request.form.has_key("post") and request.form["post"] != "":
            db_methods.addPost(request.form["title"], request.form["post"], session["username"])
        elif request.form.has_key("BlogID"):
            return render_template("myposts.html", username = session["username"], userPosts = userPosts, editing = request.form["BlogID"])
        elif request.form.has_key("edit"):
            db_methods.editUserPost(request.form["edit"], request.form["editedID"], session["username"])
        userPosts = db_methods.getUserPosts(session["username"])
        return render_template("myposts.html", username = session["username"], userPosts = userPosts)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if session.has_key("loggedIn") and session["loggedIn"]:
        session["loggedIn"] = False
    return redirect(url_for("blog"))

@app.route("/createpost")
def createpost():
    if session.has_key("loggedIn") and session["loggedIn"]:
        return render_template("createpost.html", username = session["username"])
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret_key"
    app.run(host='0.0.0.0',port=8000)
