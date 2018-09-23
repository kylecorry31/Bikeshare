class User:
	def __init__(self, student_id, email, name, bike=None):
		self.student_id = student_id
		self.email = email
		self.name = name
		self.bike = bike

	def __repr__(self):
		return "{} ({}) - ID #{}".format(self.name, self.email, self.student_id)