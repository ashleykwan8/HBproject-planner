"""Server for journal """

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

    # first_name = request.form.get('first_name')
    # last_name = request.form.get('last_name')
    username = request.form.get('username')
    password = request.form.get('password')

    user = crud.get_user_by_username(username)

    if user:
        flash('Account already exists!')
    else:
        crud.create_user(username, password)
        flash('Account created successfully!')

    return redirect('/')


@app.route('/login', methods=["POST", "GET"])
def login():
    """Logging in user."""
    username = request.form.get('login-username')
    password = request.form.get('login-password')

    
    # login_user = crud.get_user_by_username(username)
    # login_password = crud.get_user_by_password(password)

    if username == crud.get_user_by_username(username):
        flash('You are Logged In!')
        return redirect('/refresh')

    else:
        flash('Account not found!')
        return redirect('/')

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash('You are Logged Out!')
    return redirect("/")

@app.route('/refresh')
def add_todo_list():
    """View Refresh Homepage"""

    todos = crud.Todo.query.all()

    return render_template('refresh.html', todos=todos)

@app.route('/add', methods=["POST"])
def add_item():
    """Add item to ToDo List"""

    item = request.form.get('todoitem')
    crud.create_todo(item, False)

    return redirect('/refresh')

@app.route('/update', methods=["POST"])
def update_list():
    
    return redirect('/refresh')









if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)


