from flask import Blueprint, send_from_directory, send_file
import os
import mimetypes

def create_app_blueprint(folder_name: str, url_prefix: str, name: str = None):
    """
    Creates a Flask Blueprint that serves a mini React app build folder
    with support for .br and .gz precompressed assets.
    """

    base_path = os.path.join(os.path.dirname(__file__), folder_name)
    build_dir = os.path.join(base_path, "build")
    assets_dir = os.path.join(build_dir, "assets")

    bp = Blueprint(
        name or folder_name,   # <‑‑ UNIQUE BLUEPRINT NAME SUPPORT
        __name__,
        static_folder=f"{folder_name}/build/assets",
        static_url_path=f"{url_prefix}/assets"
    )

    def serve_compressed(base_path, filename):
        full = os.path.join(base_path, filename)

        # Brotli first
        if os.path.exists(full + ".br"):
            response = send_file(full + ".br")
            response.headers["Content-Encoding"] = "br"
            response.headers["Content-Type"] = mimetypes.guess_type(filename)[0] or "application/octet-stream"
            return response

        # Gzip fallback
        if os.path.exists(full + ".gz"):
            response = send_file(full + ".gz")
            response.headers["Content-Encoding"] = "gzip"
            response.headers["Content-Type"] = mimetypes.guess_type(filename)[0] or "application/octet-stream"
            return response

        # Normal file
        return send_from_directory(base_path, filename)

    @bp.route(url_prefix)
    @bp.route(f"{url_prefix}/<path:path>")
    def serve_app(path=""):
        # Serve assets
        if path.startswith("assets/"):
            filename = path[7:]
            return serve_compressed(assets_dir, filename)

        # Serve any file with an extension
        if "." in path:
            return serve_compressed(build_dir, path)

        # Serve index.html
        return send_from_directory(build_dir, "index.html")

    return bp
