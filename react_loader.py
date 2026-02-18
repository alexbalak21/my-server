from flask import Blueprint, send_from_directory
import os

def create_react_blueprint(app_name: str, url_prefix: str):
    """
    Creates a Flask Blueprint that serves a React build folder.

    app_name: folder name containing __init__.py and /build
    url_prefix: URL path (e.g. '/apps/react')
    """

    bp = Blueprint(
        app_name,
        __name__,
        static_folder=f"{app_name}/build/assets",
        static_url_path=f"{url_prefix}/assets"
    )

    BUILD_DIR = os.path.join(os.path.dirname(__file__), app_name, "build")

    @bp.route(url_prefix)
    @bp.route(f"{url_prefix}/<path:path>")
    def serve_app(path=""):
        # Serve assets
        if path.startswith("assets/"):
            return send_from_directory(os.path.join(BUILD_DIR, "assets"), path[7:])

        # Serve any file with an extension
        if "." in path:
            return send_from_directory(BUILD_DIR, path)

        # Serve index.html
        return send_from_directory(BUILD_DIR, "index.html")

    return bp
