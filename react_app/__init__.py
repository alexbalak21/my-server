from flask import Blueprint, send_from_directory
import os

react_bp = Blueprint(
    "react_app",
    __name__,
    static_folder="build/assets",
    static_url_path="/apps/react/assets"
)

# Absolute path to the build directory
BUILD_DIR = os.path.join(react_bp.root_path, "build")

@react_bp.route("/apps/react")
@react_bp.route("/apps/react/<path:path>")
def react_app(path=""):
    # Serve assets (JS, CSS, images)
    if path.startswith("assets/"):
        return send_from_directory(os.path.join(BUILD_DIR, "assets"), path[7:])

    # Serve any file with an extension (favicon, svg, etc.)
    if "." in path:
        return send_from_directory(BUILD_DIR, path)

    # Serve the React app's index.html
    return send_from_directory(BUILD_DIR, "index.html")
