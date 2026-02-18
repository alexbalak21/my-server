from flask import Flask, send_from_directory, render_template

# Import blueprints
from react_app import react_bp
from password_generator import password_bp


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="templates/assets",
    static_url_path="/assets"
)

# Register mini‑apps
app.register_blueprint(react_bp)
app.register_blueprint(password_bp)

print(app.url_map)


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
