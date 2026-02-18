from flask import Blueprint, send_from_directory
import os

password_bp = Blueprint(
    "password_generator",
    __name__,
    static_folder="build/assets",
    static_url_path="/apps/passgen/assets"
)

BUILD_DIR = os.path.join(password_bp.root_path, "build")

@password_bp.route("/apps/passgen")
@password_bp.route("/apps/passgen/<path:path>")
def password_generator(path=""):
    # Serve assets
    if path.startswith("assets/"):
        return send_from_directory(os.path.join(BUILD_DIR, "assets"), path[7:])

    # Serve files with extensions (vite.svg, etc.)
    if "." in path:
        return send_from_directory(BUILD_DIR, path)

    # Serve the mini‑app's index.html
    return send_from_directory(BUILD_DIR, "index.html")
