from flask import Flask, send_from_directory, render_template
from react_loader import create_react_blueprint


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="templates/assets",
    static_url_path="/assets"
)

# Register mini‑apps
app.register_blueprint(create_react_blueprint("react_app", "/apps/react"))
app.register_blueprint(create_react_blueprint("password_generator", "/apps/passgen"))

# --- React catch‑all route ---
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    # Serve static assets from templates/assets/
    if path.startswith("assets/"):
        return send_from_directory("templates", path)

    # Serve any file with an extension (favicon, images, etc.)
    if "." in path:
        return send_from_directory("templates", path)

    # Otherwise return index.html for React Router
    return render_template("index.html")
