from bikeshare import SystemTime
__name__ = "Logger"

def log(system_name, message):
	print("[{}] {}: {}".format(SystemTime.get_formatted_time(), system_name, message))