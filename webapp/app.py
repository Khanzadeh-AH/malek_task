import os
from pathlib import Path
from flask import Flask, render_template
import psycopg2


def connect_to_db():
    connection = psycopg2.connect(
        host="db",
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        dbname=os.environ.get("POSTGRES_DB"),
        port=5432
    )
    return connection


current_dir = Path(__file__).resolve().parent
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    pg_conn = connect_to_db()
    app.run(host="0.0.0.0", port=8080)
