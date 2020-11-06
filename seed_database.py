"""Script to seed database with test data."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb planner')
os.system('createdb planner')

model.connect_to_db(server.app

