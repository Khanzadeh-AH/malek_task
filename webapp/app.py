import os
from pathlib import Path
from flask import Flask, render_template

current_dir = Path(__file__).resolve().parent
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(current_dir / "templates/index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("WEBAPP_PORT")))
