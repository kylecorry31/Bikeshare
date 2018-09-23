from bikeshare.entities import Bike

class MockBikeShare():

	def __init__(self):
		self.bike = Bike(0, "0", "loc0", self)
		self.user = None

	def can_return_bike(self, user_id, bike_serial):
		return self.user == user_id and bike_serial == self.bike.serialNo

	def return_bike(self, user_id, bike_serial):
		self.user = None
		return True

	def can_checkout_bike(self, user_id):
		return self.user != user_id

	def checkout_bike(self, user_id, bike_serial):
		self.user = user_id
		return True

	def report_swipe(self, user_id, bike):
		pass

	def get_information(self, bike_serial):
		return ""