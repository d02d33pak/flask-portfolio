"""
Portfolio Website

Author: Deepak Talan
Github: @d02d33pak
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    """ HomePage """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
