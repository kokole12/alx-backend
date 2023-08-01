#!/usr/bin/env python3
"""A simple flask application"""


from flask import Flask
from flask import render_template


app = Flask(__name__)


"""route to the index page"""


@app.route('/', strict_slashes=False)
def index() -> str:
    """rendering the template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
