"""Script to seed database with test data."""

import os
import json
from random import choice

import crud
import model
import server

os.system('dropdb planner')
os.system('createdb planner')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/users.json') as d:
    user_data = json.loads(d.read())
with open('data/entry.json') as d:
    entry_data = json.loads(d.read())
with open('data/note.json') as d:
    note_data = json.loads(d.read())
with open('data/listname.json') as d:
    list_data = json.loads(d.read())
with open('data/account.json') as d:
    account_data = json.loads(d.read())

users_in_db = []
for user in user_data:
    username,password,first_name,last_name = (user['username'],
                                            user['password'],
                                            user['first_name'],
                                            user['last_name'])
    user_db = crud.create_user(username,
                                password)
    users_in_db.append(user_db)

login_in_db = []
for login in user_data:
    user_id = choice(users_in_db).id

    login_db = crud.create_login(user_id)
    login_in_db.append(login_db)

account_in_db = []
for account in account_data:
    email, password = (account['email'],
                        account['password'])
    login_id = choice(login_in_db).id

    account_db = crud.create_account(email,password,login_id)
    account_in_db.append(account_db)

lists_in_db = []
for newlist in list_data:
    name = (newlist['name'])
    user_id = choice(users_in_db).id
    list_db = crud.create_list(name, user_id)
    lists_in_db.append(list_db)

entries_in_db = []
for entry in entry_data:
    user_text = (entry['user_text'])
    newlist_id = choice(lists_in_db).id

    entry_db = crud.create_entry(user_text, newlist_id)
    entries_in_db.append(entry_db)

notes_in_db = []
for note in note_data:
    note_text = (note['note_text'])
    user_id = choice(users_in_db).id

    note_db = crud.create_note(note_text, user_id)
    entries_in_db.append(note_db)