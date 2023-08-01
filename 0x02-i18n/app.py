#!/usr/bin/env python3
"""simple flask application"""


from flask import Flask, render_template

app = Flask(__name__)


@app.get('/', strict_slashes=False)
def index():
    """function that loads the  root directorty"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """loading the main app server"""
    app.run(host='0.0.0.0', port=5000, debug=True)
