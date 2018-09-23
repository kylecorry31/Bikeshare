import UserDirectory
from user import User
from bike import Bike
import CardAccess
import SystemTime
from datetime import timedelta
import Logger

class BikeShare:

	def __init__(self):
		self.bikes = [
			{
				"user": None,
				"rental_start": None,
				"box": Bike(0, "Q1", "quad", self)
			},
			{
				"user": None,
				"rental_start": None,
				"box": Bike(1, "Q2", "quad", self)
			},
			{
				"user": None,
				"rental_start": None,
				"box": Bike(2, "Q3", "quad", self)
			}
		] # TODO: load bikes from DB

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

	def get_information(self, bike_serial):
		filtered = list(filter(lambda bike: bike["box"].serialNo == bike_serial, self.bikes))
		if len(filtered) == 0:
			return "Unknown bike"
		bike = filtered[0]
		user_info = "{} ({}) ID #{}".format(bike["user"].name, bike["user"].email, bike["user"].student_id) if bike["user"] is not None else ""
		return "Bike {}, {} from {}, status: {}".format(bike_serial, bike["box"].name, bike["box"].station, "active" if bike["box"].is_available() else "checked out by " + user_info)


	def __repr__(self):
		return 'Status Report\n\t' + '\n\t'.join([str(bike['box']) for bike in self.bikes])



def main():	
	bikeshare = BikeShare()

	print("============ Welcome to Gompei's Gears! ============\n")

	bikes = [bike["box"] for bike in bikeshare.bikes]
	Logger.log("BikeShare", str(bikeshare))
	print()

	while True:
		print("====================================================\n")
		action = input('Swipe card (s) or status report (r): ')
		if action[0] == 'r':
			print()
			Logger.log("BikeShare", str(bikeshare))
			print()
			continue
		student_id = int(input("Student ID: "))
		bike_number = int(input("Bike number: "))
		print()
		bikeshare.on_swipe(student_id, bike_number)
		print()
		Logger.log("BikeShare", str(bikeshare))
		print()



if __name__ == '__main__':
	main()