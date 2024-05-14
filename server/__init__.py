from flask import Flask
from router.main import main
app = Flask(__name__)

app.register_blueprint(main, url_prefix='/server/')


if __name__ == "__main__":
    app.run(debug=True)
