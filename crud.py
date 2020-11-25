"""Create, Read, Update, Delete (CRUD) operations."""

from model import db, User, Login, Account, Todo, NewList, Entry, Note, Journal, connect_to_db


if __name__== '__main__':
    from server import app
    connect_to_db(app)


def create_user(username,password):
    """Create and return a new user."""

    user = User(username= username, password = password)

    db.session.add(user)
    db.session.commit()

    return user 

def create_account(email,password,login_id):
    """Create Account."""

    account = Account(email=email, password=password, login_id=login_id)

    db.session.add(account)
    db.session.commit()

    return account

def create_login(user_id):
    """Login"""

    login = Login(user_id=user_id)

    db.session.add(login)
    db.session.commit()

    return login

def add_todo(text,complete):
    """ToDo item"""

    todo = Todo(text=text, complete=False)
    db.session.add(todo)
    db.session.commit()

    return todo

def complete_item(id):
    """Set item to complete"""

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True

    db.session.add(todo)
    db.session.commit()

    return todo

def delete_list():
    """delete the todo list"""
    
    db.session.query(Todo).delete()
    db.session.commit()

    # add a button that will do this function



def create_list(name, user_id):
    """Create an List"""

    nlist = NewList(name=name, user_id=user_id)

    db.session.add(nlist)
    db.session.commit()

    return nlist

def add_entry(id):
    """Create an Entry"""

    entry = Entry.query.filter_by(id=int(id)).first()

    db.session.add(entry)
    db.session.commit()

    return entry


def create_note(note_text, user_id):
    """Create a Note"""

    note = Note(note_text= note_text, user_id=user_id)

    db.session.add(note)
    db.session.commit()

    return note


def get_user_by_username(username):
    # print(User.query.filter(User.username == username).first())
    return User.query.filter(User.username == username).first()

def get_user_by_password(password):
    # print(User.query.filter(User.password == password).first())
    return User.query.filter(User.password == password).first()

def set_reminder_first_name(first_name):

    first_name = User(first_name = first_name)

    db.session.add(first_name)
    db.session.commit()

def set_reminder_phone_num(phone_num):

    phone_num = User(phone_num = phone_num)
    
    db.session.add(phone_num)
    db.session.commit()

def get_user_by_phone_number(phone_num):
    return User.query.filter(User.phone_num == phone_num).first()


