import sqlalchemy as sqla

engine = sqla.create_engine('sqlite:///pets.db')

engine.execute('INSERT INTO person (id, first_name, last_name, age) VALUES (1, "James", "Smith", 41)')
engine.execute('INSERT INTO person (id, first_name, last_name, age) VALUES (2, "Diana", "Greene", 23)')
engine.execute('INSERT INTO person (id, first_name, last_name, age) VALUES (3, "Sara", "White", 27)')
engine.execute('INSERT INTO person (id, first_name, last_name, age) VALUES (4, "William", "Gibson", 23)')

engine.execute('INSERT INTO pet (id, name, breed, age, dead) VALUES (1, "Rusty", "Dalmation", 4, 1)')
engine.execute('INSERT INTO pet (id, name, breed, age, dead) VALUES (2, "Bella", "Alaska Malamute", 3, 0)')
engine.execute('INSERT INTO pet (id, name, breed, age, dead) VALUES (3, "Max", "Cocker Spaniel", 1, 0)')
engine.execute('INSERT INTO pet (id, name, breed, age, dead) VALUES (4, "Rocky", "Beagle", 7, 0)')
engine.execute('INSERT INTO pet (id, name, breed, age, dead) VALUES (5, "Rufus", "Cocker Spaniel", 1, 0)')
engine.execute('INSERT INTO pet (id, name, breed, age, dead) VALUES (6, "Spot", "Bloodhound", 2, 1)')

engine.execute('INSERT INTO person_pet (person_id, pet_id) VALUES (1, 1)')
engine.execute('INSERT INTO person_pet (person_id, pet_id) VALUES (1, 2)')
engine.execute('INSERT INTO person_pet (person_id, pet_id) VALUES (2, 3)')
engine.execute('INSERT INTO person_pet (person_id, pet_id) VALUES (2, 4)')
engine.execute('INSERT INTO person_pet (person_id, pet_id) VALUES (3, 5)')
engine.execute('INSERT INTO person_pet (person_id, pet_id) VALUES (4, 6)')
