__name__ = "CardAccess"

import random
from user import User
import Logger

f = open('data/first_names.txt', 'r')
first_names = f.read().split('\n')
f.close()

f = open('data/last_names.txt', 'r')
last_names = f.read().split('\n')
last_names = [name.title() for name in last_names]
f.close()

students = []

def create_random_name():
	first = random.choice(first_names)
	last = random.choice(last_names)
	randInt = random.randint(0, 2)
	return (first, last, randInt)

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
	Logger.log("CardAccess", "ID #{} at bike {} (SerialNo: {}, Location: {})".format(student_id, bike.name, bike.serialNo, bike.station.title()))

for i in range(100):
	name = create_random_name()
	u = User(i, "{}{}{}@school.edu".format(name[0][0].lower(), name[1].lower(), name[2] if name[2] != 0 else ""), "{} {}".format(name[0], name[1]))
	add_user(u)