# My Website

Overview
This project is a modular Flask server designed to host multiple React mini‑applications under a unified backend.
Each React app is built with Vite and deployed into its own isolated folder inside the Flask project.

This architecture allows you to:

Serve multiple independent React apps (e.g., /apps/react, /apps/passgen)

Keep Python code safe from Vite’s build cleanup

Maintain clean separation between backend logic and frontend builds

Deploy new mini‑apps by simply adding a folder + blueprint

📂 Project Structure

```text
my-server/
├── app.py                  # Main Flask application
├── react_loader.py         # React loader utility
├── home/                   # Main Homepage at /
│   └── build/
│       └── index.html
...existing code...
├── react/       # React source code (Vite project)
│   ├── src/
│   │   ├── App.tsx
│   │   ├── index.css
│   │   └── main.tsx
│   ├── public/
│   │   └── favicon.svg
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   ├── vite.config.ts
│   └── README.md
├── react_app/        # Flask blueprint + built React app
│   ├── __init__.py
│   └── build/
│       ├── index.html
│       └── assets/
│           └── favicon.svg
├── password_generator/  # Another mini-app (static)
│   ├── __init__.py
│   └── build/
│       ├── index.html
│       └── assets/
│           └── favicon.svg
├── home/
│   └── build/
│       └── index.html
├── env/                    # Python virtual environment
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
├── __pycache__/
├── remove_pycache.ps1      # Utility script
├── .gitignore
└── .git/
```

🧩 How the Architecture Works
1. Flask handles routing
Each mini‑app is mounted under /apps/<name> using a Blueprint.

Example:

/apps/react → React app #1
/apps/passgen → Password generator app
/ → Main React SPA (optional)

2. React builds go into react_app/build/
Vite is configured to output directly into the Flask project:

```ts
build: {
	outDir: resolve(__dirname, '../react_app/build'),
	assetsDir: 'assets',
	emptyOutDir: true
}
```
This ensures:

Python files are never overwritten
Flask can serve the build directly
Assets resolve correctly under /apps/react/assets/*

3. Flask serves the React build
Each Blueprint exposes:

index.html
/assets/*
Any file with an extension
React Router fallback

🛠️ Installation
1. Install Python dependencies
```bash
pip install -r requirements.txt
```
2. Install React dependencies
```bash
cd react
npm install
```

🏗️ Building the React App
From the react/ folder:

```bash
npm run build
```
This outputs the production build into:

react_app/build/

▶️ Running the Flask Server
From the project root:

```bash
flask run
```
Server runs at:

http://127.0.0.1:5000

Mini‑apps:

React app → http://127.0.0.1:5000/apps/react
Password generator → http://127.0.0.1:5000/apps/passgen

🧹 Cleaning Python Cache
Use the included PowerShell script:

```bash
./remove_pycache.ps1
```

🧱 Adding a New React Mini‑App
Create a new folder:
my_new_app/

Add a Blueprint (__init__.py)

Configure Vite:

```ts
const FLASK_REACT_FOLDER = 'my_new_app'
```
Build:

```bash
npm run build
```

Register the Blueprint in app.py

Done — the new app is live under /apps/<name>.

