from flask import Blueprint, send_from_directory
import os

def create_react_blueprint(folder_name: str, url_prefix: str):
    """
    Creates a Flask Blueprint that serves a React build folder.

    folder_name: name of the folder containing /build
    url_prefix: URL path (e.g. '/apps/react')
    """

    base_path = os.path.join(os.path.dirname(__file__), folder_name)
    build_dir = os.path.join(base_path, "build")

    bp = Blueprint(
        folder_name,
        __name__,
        static_folder=f"{folder_name}/build/assets",
        static_url_path=f"{url_prefix}/assets"
    )

    @bp.route(url_prefix)
    @bp.route(f"{url_prefix}/<path:path>")
    def serve_app(path=""):
        # Serve assets
        if path.startswith("assets/"):
            return send_from_directory(os.path.join(build_dir, "assets"), path[7:])

        # Serve any file with an extension
        if "." in path:
            return send_from_directory(build_dir, path)

        # Serve index.html
        return send_from_directory(build_dir, "index.html")

    return bp
