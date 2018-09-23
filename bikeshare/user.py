class User:
	def __init__(self, student_id, email, name):
		self.student_id = student_id
		self.email = email
		self.name = name

	def __repr__(self):
		return "{} ({}) - ID #{}".format(self.name, self.email, self.student_id)