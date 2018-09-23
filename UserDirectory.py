__name__ = "UserDirectory"

import random
from user import User

first_names = ['Bob', 'Joe', 'John', 'Matt', 'Harry', 'Alice', 'Sarah', 'Jane', 'Claire', 'Amy']
last_names = ['Smith', 'Doe', 'Erikson', 'Stevens', 'Washington']

students = []

def create_random_name():
	first = random.choice(first_names)
	last = random.choice(last_names)
	return (first, last)

for i in range(5):
	name = create_random_name()
	u = User(i, "{}{}@wpi.edu".format(name[0][0].lower(), name[1].lower()), "{} {}".format(name[0], name[1]))
	students.append(u)

def lookup(student_id):
	found = list(filter(lambda student: student.student_id == student_id, students))
	if len(found) == 0:
		return None
	else:
		return found[0]

def is_valid(student_id):
	return lookup(student_id) is not None

def has_bike(student_id):
	student = lookup(student_id)
	if student:
		return student.bike is not None
	else:
		return False

def get_bike(student_id):
	student = lookup(student_id)
	if not student:
		return None
	if has_bike(student_id):
		return student.bike
	else:
		return None

def set_bike(student_id, bike):
	student = lookup(student_id)
	if not student:
		return
	student.bike = bike