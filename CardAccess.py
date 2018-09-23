__name__ = "CardAccess"

import random
from user import User
import Logger

first_names = ['Bob', 'Joe', 'John', 'Matt', 'Harry', 'Alice', 'Sarah', 'Jane', 'Claire', 'Amy']
last_names = ['Smith', 'Doe', 'Erikson', 'Stevens', 'Washington']

students = []

def create_random_name():
	first = random.choice(first_names)
	last = random.choice(last_names)
	return (first, last)

def add_user(user):
	students.append(user)

def lookup(student_id):
	found = list(filter(lambda student: student.student_id == student_id, students))
	if len(found) == 0:
		return None
	else:
		return found[0]

def is_valid(student_id):
	return lookup(student_id) is not None

def log_swipe(student_id, bike):
	Logger.log("CardAccess", "ID #{} at bike {} (SerialNo: {}, Location: {})".format(student_id, bike.name, bike.serialNo, bike.station))

for i in range(5):
	name = create_random_name()
	u = User(i, "{}{}@wpi.edu".format(name[0][0].lower(), name[1].lower()), "{} {}".format(name[0], name[1]))
	add_user(u)