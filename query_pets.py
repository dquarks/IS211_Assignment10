import sqlalchemy as sqla

engine = sqla.create_engine('sqlite:///pets.db')
text = input('Enter a person\'s ID number: ')

while text != '-1':
    result = engine.execute('SELECT id, first_name, last_name, age FROM person WHERE id = %s' % text)
    data = result.fetchall()

    if not data:
        print('User ID not found.')
    else:
        for output in data:

            person_id = output[0]
            person_age = output[3]
            first_last = '%s %s' % (output[1], output[2])
            print(first_last + ', %s years old' % person_age)

            dump1 = engine.execute('SELECT person_id, pet_id FROM person_pet WHERE person_id = %s' % person_id)
            for info in dump1.fetchall():
                pet_id = info[1]
                dump2 = engine.execute('SELECT id, name, breed, age, dead FROM pet WHERE id = %s' % pet_id)
                for pet_data in dump2.fetchall():
                    print('%s owned %s, a %s, that was %s years old.' % (first_last, pet_data[1], pet_data[2], pet_data[3]))
    text = input('Enter a person\'s ID number: ')
