#!/usr/bin/env python3
"""A simple flask app
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
async def hello_world() -> str:
    """_summary_
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
