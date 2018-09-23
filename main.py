#! /usr/bin/env python3

from bikeshare import Logger
from bikeshare.BikeShare import BikeShare

def main():
	bikeshare = BikeShare()

	print("============ Welcome to Gompei's Gears! ============\n")

	bikes = [bike["box"] for bike in bikeshare.bikes]
	Logger.log("BikeShare", str(bikeshare))
	print()

	while True:
		print("====================================================\n")
		action = input('Swipe card (s), status report (r), activate (a), deactivate (d): ')
		if action[0] == 'r':
			print()
			Logger.log("BikeShare", str(bikeshare))
			print()
			continue
		elif action[0] == 'a':
			bike_number = int(input("Activate bike number: "))
			print()
			bikeshare.on_activate_bike(bike_number)
			print()
			Logger.log("BikeShare", str(bikeshare))
			print()
			continue
		elif action[0] == 'd':
			bike_number = int(input("Deactivate bike number: "))
			print()
			bikeshare.on_deactivate_bike(bike_number)
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