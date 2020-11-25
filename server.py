"""Server for journal """

from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import random
from model import Todo
# import send_sms

AFFIRMATION = [
    'You are doing your best!', 'Be happy!','You are brave!', 'You are Bold and Beautiful!', 
    'You are Talented and Intelligent!','Be kind to yourself','Love yourself'
]

app = Flask(__name__)

app.secret_key = "ReFresh88192932392"
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
    
    if len(password) < 5:
        flash('Password needs to be at least 6 characters or more') 

    else:
        crud.create_user(username, password)
        flash('Account created successfully!')

    return redirect('/')


@app.route('/login', methods=["POST", "GET"])
def login():
    """Logging in user."""
    username = request.form.get('login-username')
    password = request.form.get('login-password')

    session['username'] = username

    login_user = crud.get_user_by_username(username)
    login_password = crud.get_user_by_password(password)
    if login_user and login_password:
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
def show_main_page():
    """View Refresh Homepage"""

    return render_template('refresh.html')

@app.route('/reminder', methods=["POST"])
def set_up_reminder():
    phone_num = request.form.get('phone_num')
    crud.set_reminder_phone_num(phone_num)

    user_phone_num = crud.get_user_by_phone_number(phone_num)
    if user_phone_num:
        import send_sms
        
    else:
        flash('Phone Number Required!')

    return redirect('/refresh')


@app.route('/todo')
def create_todo_list():
    """Show Todo List"""

    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    
    return render_template('todo.html', 
                        incomplete=incomplete, 
                        complete=complete)


@app.route('/add', methods=["POST"])
def add_item():
    """Add item to ToDo List"""

    item = request.form.get('todoitem')
    crud.add_todo(item, False)

    return redirect('/todo')


@app.route('/complete/<id>')
def complete_item(id):

    crud.complete_item(id)

    return redirect('/todo')


@app.route('/delete')
def delete_list():
    """Delete complete items"""

    crud.delete_list()

    return redirect('/todo')


@app.route('/journal')
def show_journal_page():
    """View Journal page"""
    
    return render_template('journal.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)


