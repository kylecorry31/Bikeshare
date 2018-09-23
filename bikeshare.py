import UserDirectory
from bikeshare_entities import User, Bike

def main():
	user = UserDirectory.lookup(1234) # load from database, given student ID
	user2 = UserDirectory.lookup(0)
	bikes = [Bike(0, "Q1", "quad"), Bike(1, "Q2", "quad"), Bike(2, "Q3", "quad")] # load all from database
	
	print('\n'.join([str(bike) for bike in bikes]))

	print()
	user.checkout(bikes[0])
	print('\n'.join([str(bike) for bike in bikes]))

	print()
	user2.checkout(bikes[0])
	user.checkout(bikes[1])
	print('\n'.join([str(bike) for bike in bikes]))

	print()
	user.end_rental()
	user2.checkout(bikes[0])
	user.checkout(bikes[1])
	print('\n'.join([str(bike) for bike in bikes]))



if __name__ == '__main__':
	main()