# Bikeshare

A python implementation of a bikeshare system with simple checkouts user an ID card swipe.

### States (Bike)
1. Active, no user
	- On valid ID swipe and user doesn't have a bike checked out, state 2 / beep, flash green, unlock box for 5 seconds, start timer
	- On invalid ID swipe or user has a bike checked out, state 1 / beep, flash red
	- On deactivate, state 3
2. Active, user
	- On ID swipe and user has this bike checked out, state 1 / beep, flash green, unlock box for 5 seconds, stop timer
	- On invalid ID swipe or valid ID swipe and user does not have this bike checked out, state 2 / beep, flash red
	- On deactivate, state 4 / send maintenance email
	- On time limit reached, state 2 / send overdue email
3. Out of order, no user
	- On ID swipe, state 3 / beep, flash red
	- On activate, state 1
4. Out of order, user
	- On ID swipe and user has this bike checked out, state 3 / beep, flash green, unlock box for 5 seconds, stop timer
	- On activate, state 2
	- On time limit reached, state 4 / send overdue email

### States (User)
1. Active
	- On ban, state 3 / remove ID from system
3. Banned
	- On unban, state 1 / add ID into system

## Usage
Install the dependencies:
```
python3 -m pip install -r requirements.txt
```

Run the main.py file as such:

```
python3 main.py
```

## Credits
Just me for now, but help is always welcome!

## Contribute
Please feel free to contribute to this project, or if you find an issue be sure to report it under issues.

## License
This project is licensed under the [MIT License](License).
