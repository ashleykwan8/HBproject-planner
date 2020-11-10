
"""Models for planner app."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__= 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    # login = db.relationship('Login', backref='user')
    # list = db.relationship('List', backref='user')
    # note = db.relationship('Note, backref='user')



    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'


class Login(db.Model):
    """Login information."""

    __tablename__= 'logins'

    login_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', backref = 'logins')

    def __repr__(self):
        return f'<Login login_id={self.login_id}>'


class Account(db.Model):
    """Google Calendar Account."""

    __tablename__= 'accounts'
    account_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    login_id = db.Column(db.Integer, db.ForeignKey('logins.login_id'))

    login = db.relationship('Login', backref = 'accounts')

    def __repr__(self):
        return f'<Account account_id={self.account_id} email={self.email}>'


class List(db.Model):
    """To-Do list."""

    __tablename__= 'lists'

    list_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', backref = 'lists')

    def __repr__(self):
        return f'<List list_id={self.list_id}>'


class Entry(db.Model):
    """"To-Do List entries."""

    __tablename__= 'entries'

    entry_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_text = db.Column(db.Text)
    # entry_status = db.Column(db.Enum)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.list_id'))

    list = db.relationship('List', backref = 'entries')

    def __repr__(self):
        return f'<Entry entry_id={self.entry_id} user_text={self.user_text}>'


class Note(db.Model):
    """Notes section"""

    __tablename__= 'notes'

    note_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    note_text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', backref = 'notes')

    def __repr__(self):
        return f'<Note note_id={self.note_id}>'



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