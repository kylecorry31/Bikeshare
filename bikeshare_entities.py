class User:
	def __init__(self, student_id, email, name, bike=None):
		self.student_id = student_id
		self.email = email
		self.name = name
		self.bike = bike

	def checkout(self, bike):
		if bike.is_available() and self.bike is None:
			bike.user = self
			self.bike = bike
			bike.unlock()
			return True
		else:
			return False

	def end_rental(self):
		if self.bike:
			self.bike.unlock()
			self.bike.user = None
			self.bike = None

	def __repr__(self):
		return "{} ({}) - ID #{}".format(self.name, self.email, self.student_id)

class Bike:
	def __init__(self, serialNo, name, station, user=None):
		self.serialNo = serialNo
		self.name = name
		self.station = station
		self.user = user

	def unlock(self):
		print("Bike {}: unlocked by {}".format(self.name, self.user.name))

	def is_available(self):
		return self.user is None

	def __repr__(self):
		return "Bike {}, {} from {}, status: {}".format(self.serialNo, self.name, self.station, "active" if self.is_available() else "checked out by {}".format(self.user))