from enum import Enum
import UserDirectory

class BikeState(Enum):
	ACTIVE_NO_USER = 1
	ACTIVE_USER = 2
	OUT_OF_ORDER_NO_USER = 3
	OUT_OF_ORDER_USER = 4

class Bike:
	def __init__(self, serialNo, name, station, user=None):
		self.state = BikeState.ACTIVE_NO_USER
		self.serialNo = serialNo
		self.name = name
		self.station = station
		self.user = user

	def on_swipe(self, user_id):
		valid = UserDirectory.is_valid(user_id)
		if self.state is BikeState.ACTIVE_NO_USER:
			# A valid swipe is a swipe who's user isn't banned
			if valid and not UserDirectory.has_bike(user_id):
				# flash and beep
				self.user = UserDirectory.lookup(user_id)
				self.unlock()
				UserDirectory.set_bike(user_id, self.serialNo)
				# start timer
				self.state = BikeState.ACTIVE_USER
			else:
				# flash and beep
				pass
		elif self.state is BikeState.ACTIVE_USER:
			if UserDirectory.get_bike(user_id) == self.serialNo:
				# flash and beep
				self.unlock()
				UserDirectory.set_bike(user_id, None)
				self.user = None
				# stop timer
				self.state = BikeState.ACTIVE_NO_USER
			else:
				# flash and beep
				pass

	def unlock(self):
		print("Bike {}: unlocked by {}".format(self.name, self.user.name))

	def is_available(self):
		return self.state == BikeState.ACTIVE_NO_USER

	def __repr__(self):
		return "Bike {}, {} from {}, status: {}".format(self.serialNo, self.name, self.station, "active" if self.is_available() else "checked out by {}".format(self.user))