__name__ = "UserDirectory"

import random
from bikeshare_entities import User

first_names = ['Bob', 'Joe', 'John', 'Matt', 'Harry', 'Alice', 'Sarah', 'Jane', 'Claire', 'Amy']
last_names = ['Smith', 'Doe', 'Erikson', 'Stevens', 'Washington']

def create_random_name():
	first = random.choice(first_names)
	last = random.choice(last_names)
	return (first, last)

def lookup(student_id):
	name = create_random_name()
	return User(student_id, "{}{}@wpi.edu".format(name[0][0].lower(), name[1].lower()), "{} {}".format(name[0], name[1]))