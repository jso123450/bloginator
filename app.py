from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

#This will be the general blog (before logging in)
@app.route("/")
def blog():
    if session.has_key("loggedIn") and session["loggedIn"]:
        return render_template("blog.html", loggedIn = True)
    else:
        return render_template("blog.html", loggedIn = False)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.form.has_key("username") and request.form.has_key("password"):
        if request.form["username"] == "user1" and request.form["password"] == "pass1":
            session["loggedIn"] = True
            return redirect(url_for("blog"))
        else:
            return render_template("login.html", error = "Invalid username or password")
    else:
        if session.has_key("loggedIn") and session["loggedIn"]:
            return redirect(url_for("blog"))
        else:
            return render_template("login.html")

@app.route("/page2")
def page2():
    if session.has_key("loggedIn") and session["loggedIn"]:
        return render_template("page2.html")
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if session.has_key("loggedIn") and session["loggedIn"]:
        session["loggedIn"] = False
    return redirect(url_for("blog"))

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret_key"
    app.run()
