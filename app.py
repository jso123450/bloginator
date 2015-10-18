from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

#This will be the general blog (before logging in)
@app.route("/")
def blog():
    if session.has_key("loggedIn") and session["loggedIn"]:
        return render_template("blog.html", loggedIn = True, username = session["username"])
    else:
        return render_template("blog.html", loggedIn = False)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.form.has_key("username") and request.form.has_key("password"):
        if request.form["username"] == "user1" and request.form["password"] == "pass1":
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

@app.route("/myposts")
def myposts():
    if session.has_key("loggedIn") and session["loggedIn"]:
        return render_template("myposts.html", username = session["username"])
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
    app.run(host='0.0.0.0', port=8000)
