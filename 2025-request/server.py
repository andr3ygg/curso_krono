from flask import Flask
import sys
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hola Mundo </p>"


hola()
