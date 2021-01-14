import flask
import pika
from datetime import datetime
import root_script
from nested import script as nested_script

app = flask.Flask(__name__)


@app.route("/")
def index():
    rt = nested_script.say_hello()
    nt = root_script.say_hello()
    return "Hello, World!" + rt + nt


if __name__ == "__main__":
    app.run(debug=True)
