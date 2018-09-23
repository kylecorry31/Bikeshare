from enum import Enum
import Logger

class BikeState(Enum):
	ACTIVE_NO_USER = 1
	ACTIVE_USER = 2
	OUT_OF_ORDER_NO_USER = 3
	OUT_OF_ORDER_USER = 4

class Bike:
	def __init__(self, serialNo, name, station, bikeshare):
		self.state = BikeState.ACTIVE_NO_USER
		self.serialNo = serialNo
		self.name = name
		self.station = station
		self.bikeshare = bikeshare

	def on_swipe(self, user_id):
		self.bikeshare.report_swipe(user_id, self)
		if self.state is BikeState.ACTIVE_NO_USER:
			# A valid swipe is a swipe who's user isn't banned
			if self.bikeshare.can_checkout_bike(user_id):
				# flash and beep
				self.bikeshare.checkout_bike(user_id, self.serialNo)
				self.unlock()
				# start timer
				self.state = BikeState.ACTIVE_USER
			else:
				# flash and beep
				pass
		elif self.state is BikeState.ACTIVE_USER:
			if self.bikeshare.can_return_bike(user_id, self.serialNo):
				# flash and beep
				self.unlock()
				self.bikeshare.return_bike(user_id, self.serialNo)
				# stop timer
				self.state = BikeState.ACTIVE_NO_USER
			else:
				# flash and beep
				pass

	def unlock(self):
		Logger.log("Bike {}".format(self.serialNo), "unlocked")

	def is_available(self):
		return self.state == BikeState.ACTIVE_NO_USER

	def __repr__(self):
		return self.bikeshare.get_information(self.serialNo)
