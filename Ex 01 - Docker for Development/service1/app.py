import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f'<h2>This is the FIRST service.<br/>{datetime.datetime.now()}</h2>'