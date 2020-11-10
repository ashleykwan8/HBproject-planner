"""Script to seed database with test data."""

import os
import json
from random import choice, randint

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


users_in_db = []
for user in user_data:
    username,password,first_name,last_name = (user['username'],
                                            user['password'],
                                            user['first_name'],
                                            user['last_name'])
    user_db = crud.create_user(username,
                                password,
                                first_name,
                                last_name)
    users_in_db.append(user_db)


entries_in_db = []
for entry in entry_data:
    user_text = (entry['user_text'])

    entry_db = crud.create_entry(user_text)
    entries_in_db.append(entry_db)


notes_in_db = []
for note in note_data:
    note_text = (note['note_text'])

    note_db = crud.create_note(user_text)
    entries_in_db.append(note_db)