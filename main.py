from flask import Flask, send_from_directory, send_file
from app_loader import create_app_blueprint
import os
import mimetypes

app = Flask(__name__)

# Homepage build folder
HOME_BUILD_DIR = os.path.join(os.path.dirname(__file__), "home", "build")
HOME_ASSETS_DIR = os.path.join(HOME_BUILD_DIR, "assets")

# Register mini‑apps with UNIQUE blueprint names
app.register_blueprint(create_app_blueprint("react_app", "/apps/react", name="react_app_main"))
app.register_blueprint(create_app_blueprint("password_generator", "/apps/passgen", name="passgen_main"))
app.register_blueprint(create_app_blueprint("password_generator", "/passgen", name="passgen_short"))


def serve_compressed(base_path, filename):
    full = os.path.join(base_path, filename)

    if os.path.exists(full + ".br"):
        response = send_file(full + ".br")
        response.headers["Content-Encoding"] = "br"
        response.headers["Content-Type"] = mimetypes.guess_type(filename)[0] or "application/octet-stream"
        return response

    if os.path.exists(full + ".gz"):
        response = send_file(full + ".gz")
        response.headers["Content-Encoding"] = "gzip"
        response.headers["Content-Type"] = mimetypes.guess_type(filename)[0] or "application/octet-stream"
        return response

    return send_from_directory(base_path, filename)


# --- Homepage (root) React app ---
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_home(path):
    if path.startswith("assets/"):
        filename = path[7:]
        return serve_compressed(HOME_ASSETS_DIR, filename)

    if "." in path:
        return serve_compressed(HOME_BUILD_DIR, path)

    return send_from_directory(HOME_BUILD_DIR, "index.html")
