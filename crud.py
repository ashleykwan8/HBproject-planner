"""Create, Read, Update, Delete (CRUD) operations."""

from model import db, User, Login, Account, Todo, NewList, Entry, Note, connect_to_db


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
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True

    db.session.add(todo)
    db.session.commit()

    return todo


def create_list(name, user_id):
    """Create an List"""

    nlist = NewList(name=name, user_id=user_id)

    db.session.add(nlist)
    db.session.commit()

    return nlist

def create_entry(user_text, newlist_id):
    """Create an Entry"""

    entry = Entry(user_text=user_text, newlist_id=newlist_id)

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


