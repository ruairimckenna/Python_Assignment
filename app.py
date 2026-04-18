import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session

load_dotenv()

app = Flask(__name__)
app.secret_key = "test"
app.debug = False
















if __name__ == "__main__":
    debug_flag = str(os.environ.get("DEBUG", "False")).lower() in ("1", "true", "yes")
    app.run(debug=debug_flag)

    