import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu