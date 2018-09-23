import UserDirectory
from user import User
from bike import Bike

def main():
	bikes = [Bike(0, "Q1", "quad"), Bike(1, "Q2", "quad"), Bike(2, "Q3", "quad")] # load all from database
	
	print('\n'.join([str(bike) for bike in bikes]))

	print()
	bikes[0].on_swipe(0)
	print('\n'.join([str(bike) for bike in bikes]))

	print()
	bikes[0].on_swipe(1)
	bikes[1].on_swipe(0)
	print('\n'.join([str(bike) for bike in bikes]))

	print()
	bikes[0].on_swipe(0)
	bikes[0].on_swipe(1)
	print('\n'.join([str(bike) for bike in bikes]))



if __name__ == '__main__':
	main()