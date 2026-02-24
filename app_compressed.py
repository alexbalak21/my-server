from flask import Flask, send_from_directory
from react_loader import create_react_blueprint
from flask_compress import Compress
import os

app = Flask(__name__)

# Load compression config from external file 
app.config.from_pyfile("compress_config.py")

# Enable compression only if COMPRESSED = True
if app.config.get("COMPRESSED", False):
    Compress(app)

# Path to your homepage build folder
HOME_BUILD_DIR = os.path.join(os.path.dirname(__file__), "home", "build")

# Remove Content-Length header only when compression is enabled
@app.after_request
def remove_content_length(response):
    if app.config.get("COMPRESSED", False):
        response.headers.pop("Content-Length", None)
    return response

# Register mini‑apps
app.register_blueprint(create_react_blueprint("react_app", "/apps/react"))
app.register_blueprint(create_react_blueprint("password_generator", "/apps/passgen"))

# --- Homepage (root) React app ---
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_home(path):
    if path.startswith("assets/"):
        return send_from_directory(os.path.join(HOME_BUILD_DIR, "assets"), path[7:])

    if "." in path:
        return send_from_directory(HOME_BUILD_DIR, path)

    return send_from_directory(HOME_BUILD_DIR, "index.html")
