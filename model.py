
"""Models for journal app."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__= 'users'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    # first_name = db.Column(db.String)
    # last_name = db.Column(db.String)

    logins = db.relationship('Login', backref='login_user')
    lists = db.relationship('NewList', backref='newlist_user')
    notes = db.relationship('Note', backref='note_user')


    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'


class Login(db.Model):
    """Login information."""

    __tablename__= 'logins'

    id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    accounts = db.relationship('Account', backref='account_login')

    def __repr__(self):
        return f'<Login login_id={self.login_id}>'


class Account(db.Model):
    """Google Calendar Account."""

    __tablename__= 'accounts'
    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    login_id = db.Column(db.Integer, db.ForeignKey('logins.id'))

    def __repr__(self):
        return f'<Account account_id={self.account_id} email={self.email}>'

class Todo(db.Model): 
    __tablename__= 'todos'
    id = db.Column(db.Integer, primary_key=True) 
    text = db.Column(db.String(200)) 
    complete = db.Column(db.Boolean) 
  
    def __repr__(self): 
        return f'<ToDo text={self.text} complete={self.complete}>'

class NewList(db.Model):
    """To-Do list."""

    __tablename__= 'lists'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    entries = db.relationship('Entry', backref='entry_list')

    def __repr__(self):
        return f'<NewList list_id={self.list_id} user_id={self.user_id}>'


class Entry(db.Model):
    """"Journaling entries."""

    __tablename__= 'entries'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    text = db.Column(db.Text)
    # entry_status = db.Column(db.Enum)
    newlist_id = db.Column(db.Integer, db.ForeignKey('lists.id'))

    def __repr__(self):
        return f'<Entry entry_id={self.entry_id} entry_text={self.user_text}>'


class Note(db.Model):
    """Notes section"""

    __tablename__= 'notes'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    note_text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Note note_id={self.note_id} user_id={self.user_id}>'

class Journal(db.Model): 
    __tablename__= 'journals'
    id = db.Column(db.Integer, primary_key=True) 
    text = db.Column(db.String(200)) 
    complete = db.Column(db.Boolean) 
  
    def __repr__(self): 
        return f'<Journal text={self.text} complete={self.complete}>'

def connect_to_db(flask_app, db_uri='postgresql:///planner', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)