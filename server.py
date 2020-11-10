"""Server for student planner """

from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage"""

    return render_template("homepage.html")

@app.route('/users', methods=["POST"])
def register_user(): 

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    password = request.form.get('password')

    user = crud.get_user_by_username(username)

    if user:
        flash('Username already exists!')
    else:
        crud.create_user(username, password, first_name, last_name)
        flash('Account created successfully!')

    return render_template("createuser.html")

# @app.route('/users')
# def user_login():

#     email = request.form.get('login-username')
#     password = request.form.get('login-password')

#     user= crud.get_user_by_email(email)
#     login_password = crud.get_user_by_password(password)

#     session['user'] = User.user_id

#     if user:
#         flash('Logged in!')

#     else:
#         flash('Need to create an account!')

#     return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)




























if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)