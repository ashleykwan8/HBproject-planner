"""Server for student planner """

from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import random

AFFIRMATION = [
    'You are doing your best!', 'You choose to be happy!', 'You are proud of youself.',
    'You are brave!', 'You are Bold and Beautiful!', 'You are Talented and Intelligent!',
    'You will be kind to yourself.', 'You love yourself.', 'You are grateful for all that you have.'
]

app = Flask(__name__)

app.secret_key = "still"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage"""

    affirmation = random.choice(AFFIRMATION)

    return render_template("homepage.html", affirmation=affirmation)


@app.route('/users', methods=["POST"])
def create_user(): 
    """Create User"""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    password = request.form.get('password')
    session["user"] = username

    user = crud.get_user_by_username(username)

    if user:
        flash('Username already exists!')
    else:
        crud.create_user(username, password, first_name, last_name)
        flash('Account created successfully!')
        return redirect('/login')

    return redirect('/')


@app.route('/login')
def user_login():
    """Logging in user."""

    username = request.form.get('login-username')
    password = request.form.get('login-password')

    user= crud.get_user_by_username(username)
    login_password = crud.get_user_by_password(password)

    return render_template('login.html')

    if user and login_password:
        flash('Logged in!')
        return redirect('/stilljournal')

    else:
        flash('Account not found!')
        return redirect('/login')
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

@app.route('/stilljournal')
def access_still_journal():
    """View Still Page"""

    return render_template('still.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)


