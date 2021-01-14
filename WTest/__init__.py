from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy as mysql
import math

app = Flask(__name__)

def calc_Pagecnt(num, artCnt):
    if num < artCnt:
        return 1
    else :
        return math.ceil(num/artCnt)
app.jinja_env.globals.update(page_Cnt=calc_Pagecnt)

app.config["SQLALCHEMY_DATABASE_URI"] = 

@app.route("/")
def index():
    return render_template("index.html", username=["wha","chu","go","na","du"], usernick=["와","츄","고","나","두"], page=1, artCnt=3)

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
