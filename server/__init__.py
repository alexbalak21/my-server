from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/server/')
def hello_world():
    return "<h1>Hello from my Flask server !</h1>"

if __name__ == "__main__":
  app.run(debug=True)

