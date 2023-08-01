#!/usr/bin/env python3
"""
    simple flask application transilated in
    english and french
"""


from flask import Flask, request, g
from flask import render_template
from flask_babel import Babel


class Config(object):
    """declaring the babel configurations"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """implementing the logic to get a user from the dictionary"""
    ID = request.args.get('login_as')
    if ID:
        return users.get(int(ID))
    return None


@app.before_request
def before_request() -> None:
    """
        method to run before the get user is invoked to
        check if there is a loggedin user
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """implementing the get best match to get languages support"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """rending the template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
