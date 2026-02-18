from flask import Blueprint, send_from_directory

password_bp = Blueprint(
    "password_generator",
    __name__,
    template_folder=".",
    static_folder="assets",
    static_url_path="/password_generator/assets"
)

@password_bp.route("/apps/passgen")
@password_bp.route("/apps/passgen/<path:path>")
def password_generator(path=""):
    # Serve assets
    if path.startswith("assets/"):
        return send_from_directory(password_bp.root_path, path)

    # Serve files with extensions (vite.svg, etc.)
    if "." in path:
        return send_from_directory(password_bp.root_path, path)

    # Serve the mini‑app's index.html
    return send_from_directory(password_bp.root_path, "index.html")
