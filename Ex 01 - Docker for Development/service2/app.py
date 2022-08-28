import datetime
from flask import Flask

print("Inside SECOND service")

app = Flask(__name__)

@app.route('/')
def hello():
    return f'<h2>This is the SECOND service.<br/>{datetime.datetime.now()}</h2>'