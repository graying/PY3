import random

from flask import Flask, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# configurations are moved to config.py class BaseConfig
# app.secret_key = "this_is_key"
# app.config["DEBUG"] = True
# app.database = "sample_sqlite3.db"
# SQLALCHEMY_DATABASE_URI = "sqlite:///sample_SQLAlchemy.db"
app.config.from_object("config.BaseConfig")
db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return "{}".format(self.title)


@app.route('/')
def index():
    flash('Hello! you are in home page')
    r = random.randint(1, 1000)
    flash(str(r))
    print(r)
    return render_template("index.html", randint=str(r))


@app.route("/show_db")
def show_db():
    posts = Post.query.all()
    flash("showing db content in show_db page")
    return render_template("show_db.html", posts=posts)


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    flash("input title/description ")
    return render_template("add_post.html")


@app.route("/submit_post", methods=["POST"])
def submit_post():
    title = request.form["title"]
    description = request.form["description"]
    db.session.add(Post(title, description))
    db.session.commit()
    flash("submitted your post and save in database")
    return render_template("submit_post.html", title=title)


if __name__ == "__main__":
    app.run()
