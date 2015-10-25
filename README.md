<h1>Bloginator</h1>

<hr> <h1> NEW </h1>
<ul>
 <li> Johnny So: Leader </li>
 <li> Vivian Li: UX </li>
 <li> Darwin Chiu: Middleware </li>
 <li> Ishraq Bhuiyan: Backend </li>
</ul>

<h2> Changelog </h2>
 - Oct 22
   - Forked original REPO
 - Oct 23
   - Started rewriting some SQLite db methods in Mongo
      - checkUserMongo(un,pw) ; countUsersMongo() ; addUserMongo()

<hr> <h1> ORIGINAL </h1>
<h2>Created by:</h2>

<p>Mark Kharakh <i>Leader</i> </p>
<p>Caitlin Stanton <i>UX</i> </p>
<p>Liam Daly <i>Backend</i> </p>
<p>Isaac Gerstein <i>Middleware</i> </p>

<h2>What is it:</h2>

<p>
 Bloginator is a web app run on Flask and with its information
 stored in a SQL database. Before logging in, visitors can see
 all blog posts ever created by every user. After logging in, users
 are able to create new posts or edit old ones. This updates the 
 information in the SQL database.
</p>

<h2>What can you do:</h2>
- Click on "Login" in the navigation bar or "Come and "Contribute" on the 
"Home" page
- Either sign in with an existing account or create a new one (done by clicking
on "Create User")
- Whether or not you are logged in will affect what you can see on the site, 
including pages and links in the navigation bar (such as "My Posts" and "Create")
- Read all users' posts on the "Home" page
- To view your specific posts, click on "My Posts" in the navigation bar
- If you want to create a new post, click on "Create" in the navigation bar or 
on the "Home" or "My Posts" pages

<h2>How to run it:</h2>
1. Have git and flask installed (from the virtualenv)
2. Navigate to the appropriate path in your terminal
3. Run "git clone git@github.com:caitlinstanton/bloginator.git"
4. Run "python app.py"
5. Go to localhost:8000 in the browser of your choice
6. ENJOY
