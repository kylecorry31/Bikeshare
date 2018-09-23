from bikeshare.entities import User, Bike, BikeState
from bikeshare import CardAccess, SystemTime, Logger
import csv
from datetime import timedelta

class BikeShare:

	def __init__(self):
		self.bikes = []
		with open('data/bikes.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				bike = {
					"user": None,
					"rental_start": None,
					"box": Bike(int(row[0]), row[1], row[2], self)
				}
				self.bikes.append(bike)

	def _has_bike(self, user_id):
		return len(list(filter(lambda bike: bike["user"] is not None and bike["user"].student_id == user_id, self.bikes))) != 0

	def can_return_bike(self, user_id, bike_serial):
		filtered = list(filter(lambda bike: bike["box"].serialNo == bike_serial, self.bikes))
		if len(filtered) == 0:
			return False
		bike = filtered[0]
		return bike["user"] is not None and bike["user"].student_id == user_id

	def return_bike(self, user_id, bike_serial):
		filtered = list(filter(lambda bike: bike["box"].serialNo == bike_serial, self.bikes))
		if len(filtered) == 0:
			return False
		user = filtered[0]["user"]
		start_time = filtered[0]["rental_start"]
		filtered[0]["user"] = None
		filtered[0]["rental_start"] = None
		total_time = timedelta(seconds=round(SystemTime.get_time() - start_time))
		Logger.log("BikeShare", "{} ({}) has returned bike {} (Rental length: {})".format(user.name, user.email, filtered[0]["box"].name, total_time))
		return True

	def can_checkout_bike(self, user_id):
		return CardAccess.is_valid(user_id) and not self._has_bike(user_id)

	def checkout_bike(self, user_id, bike_serial):
		filtered = list(filter(lambda bike: bike["box"].serialNo == bike_serial, self.bikes))
		if len(filtered) == 0:
			return False
		user = CardAccess.lookup(user_id)
		filtered[0]["user"] = user
		filtered[0]["rental_start"] = SystemTime.get_time()
		Logger.log("BikeShare", "{} ({}) has checked out bike {}".format(user.name, user.email, filtered[0]["box"].name))
		return True

	def report_swipe(self, user_id, bike):
		CardAccess.log_swipe(user_id, bike)

	def on_swipe(self, user_id, bike_serial):
		filtered = list(filter(lambda bike: bike["box"].serialNo == bike_serial, self.bikes))
		if len(filtered) == 0:
			return
		filtered[0]['box'].on_swipe(user_id)

	def on_deactivate_bike(self, bike_serial):
		filtered = list(filter(lambda bike: bike["box"].serialNo == bike_serial, self.bikes))
		if len(filtered) == 0:
			return
		filtered[0]['box'].on_deactivate()

	def on_activate_bike(self, bike_serial):
		filtered = list(filter(lambda bike: bike["box"].serialNo == bike_serial, self.bikes))
		if len(filtered) == 0:
			return
		filtered[0]['box'].on_activate()

	def get_information(self, bike_serial):
		filtered = list(filter(lambda bike: bike["box"].serialNo == bike_serial, self.bikes))
		if len(filtered) == 0:
			return "Unknown bike"
		bike = filtered[0]
		user_info = "{} ({}) ID #{}".format(bike["user"].name, bike["user"].email, bike["user"].student_id) if bike["user"] is not None else ""
		status = ""
		if bike['box'].state == BikeState.ACTIVE_NO_USER:
			status = "Active - available"
		elif bike['box'].state == BikeState.ACTIVE_USER:
			status = "Active - checked out by " + user_info
		elif bike['box'].state == BikeState.OUT_OF_ORDER_NO_USER:
			status = "Inactive"
		elif bike['box'].state == BikeState.OUT_OF_ORDER_USER:
			status = "Inactive - checked out by " + user_info

		return "{}\t{}\t{}".format(bike_serial, bike["box"].name, status)


	def __repr__(self):
		return 'Status Report\n\tNo.\tName\tStatus\t\n\t' + '\n\t'.join([str(bike['box']) for bike in self.bikes])
