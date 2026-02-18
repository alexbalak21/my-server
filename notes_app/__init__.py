from flask import Blueprint, send_from_directory

notes_bp = Blueprint(
    "notes",
    __name__,
    template_folder=".",
    static_folder="assets",
    static_url_path="/notes/assets"
)

@notes_bp.route("/apps/notes")
@notes_bp.route("/apps/notes/<path:path>")
def notes(path=""):
    # Serve static assets
    if path.startswith("assets/"):
        return send_from_directory(notes_bp.root_path, path)

    # Serve files with extensions (vite.svg, images, etc.)
    if "." in path:
        return send_from_directory(notes_bp.root_path, path)

    # Serve the mini‑app's own index.html
    return send_from_directory(notes_bp.root_path, "index.html")
