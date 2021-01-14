from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", username=["wha", "chu", "go", "na", "du?"], usernick=["와", "츄", "고", "나", "두?"], page=2, artCnt=3)


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
