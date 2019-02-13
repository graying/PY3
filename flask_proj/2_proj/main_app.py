import random

from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = "thisisiskey"
app.config["DEBUG"] = True


@app.route('/')
def index():
    flash('Hello! you are in home page')
    rint = random.randint(1, 1000)
    flash(str(rint))
    print(rint)
    return render_template("index.html", randint=str(rint))


if __name__ == "__main__":
    app.run()
