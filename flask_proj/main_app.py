from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///flask_app.db"
app.config["DEBUG"] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

@app.route('/')
def index():
    users = User.query.all()
    return render_template("index.html", users=users)
    # return "<h1 style='color: red'>hello flask...</h1>"

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).all() # all() return a list
    if len(user)==0:
        return "no found"
    return render_template("profile.html", user=user[0]) # past only the first element to display

@app.route("/post_user", methods=["POST"])
def post_user():
    username = request.form["username"]
    email = request.form["email"]
    user = User(username, email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run()
