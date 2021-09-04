"""Script to seed database."""

from faker import Faker
import os
from datetime import datetime

import crud
import model
import server


os.system('dropdb melon_reservations')
os.system('createdb melon_reservations')

model.connect_to_db(server.app)
model.db.create_all()


users_in_db = []
reservations_in_db = []
fake = Faker()
# Creting 5 fake users to be added to the users table in the database
for i in range(5):
    first_name = fake.first_name()
    last_name = fake.last_name()
    user_name = first_name
    email = f'{user_name}{i}@gmail.com'
    password = f'test'
    chosen_date = fake.date()
    chosen_time = fake.time()

    user = crud.create_user(first_name, last_name, user_name, email, password)
    users_in_db.append(user)
    
    # Creating 5 fake user reservations to be added to the reservations table in the database
    reservation = crud.create_reservation(chosen_date, chosen_time, user)
    reservations_in_db.append(reservation)    
