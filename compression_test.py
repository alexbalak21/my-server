from flask import Flask
from flask_compress import Compress

app = Flask(__name__)

# Enable compression
Compress(app)

@app.route("/")
def hello_world():
    return "Hello, World! (compressed)"
