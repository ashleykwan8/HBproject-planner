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


