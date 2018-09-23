import time
import datetime

__name__ = "SystemTime"


def get_time():
	return time.time()

def get_formatted_time():
	now = datetime.datetime.now()
	return now.strftime("%m-%d-%y %I:%M:%S %p")