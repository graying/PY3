import random
import sqlite3

from flask import g, Flask, render_template, flash

app = Flask(__name__)
app.secret_key = "thisisiskey"
app.config["DEBUG"] = True
app.database = "sample_sqlite3.db"


@app.route('/')
def index():
    flash('Hello! you are in home page')
    rint = random.randint(1, 1000)
    flash(str(rint))
    print(rint)
    return render_template("index.html", randint=str(rint))


@app.route("/show_db")
def show_db():
    g.db = sqlite3.connect("sample_sqlite3.db")
    cur = g.db.execute("select * from posts")
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    flash("showing db content in show_db page")
    return render_template("show_db.html", posts=posts)


if __name__ == "__main__":
    app.run()
