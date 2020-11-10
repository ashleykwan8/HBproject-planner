"""Create, Read, Update, Delete (CRUD) operations."""

from model import db, User, Login, Account, Entry, Note, connect_to_db

#Functions start here!

if __name__== '__main__':
    from server import app
    connect_to_db(app)


def create_user(username,password,first_name,last_name):
    """Create and return a new user."""

    user = User(username= username, password = password, 
                first_name=first_name, last_name=last_name)

    db.session.add(user)
    db.session.commit()

    return user 


def create_entry(user_text):
    """Create an Entry"""

    entry= Entry(user_text= user_text)

    db.session.add(entry)
    db.session.commit()

    return entry


def create_note(user_text):
    """Create a Note"""

    note = Note(note_text= note_text)

    db.session.add(note)
    db.session.commit()

    return note


def get_user_by_email(email):

    return User.query.filter(User.email == email).first()


