from flask import Flask, send_from_directory
from react_loader import create_react_blueprint
import os

app = Flask(__name__)

# Path to your homepage build folder
HOME_BUILD_DIR = os.path.join(os.path.dirname(__file__), "home", "build")

# Register mini‑apps
app.register_blueprint(create_react_blueprint("react_app", "/apps/react"))
app.register_blueprint(create_react_blueprint("password_generator", "/apps/passgen"))

# --- Homepage (root) React app ---
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_home(path):
    # Serve assets
    if path.startswith("assets/"):
        return send_from_directory(os.path.join(HOME_BUILD_DIR, "assets"), path[7:])

    # Serve any file with an extension (favicon, images, etc.)
    if "." in path:
        return send_from_directory(HOME_BUILD_DIR, path)

    # Otherwise return index.html for React Router
    return send_from_directory(HOME_BUILD_DIR, "index.html")
