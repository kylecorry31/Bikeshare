from bikeshare import SystemTime
__name__ = "Logger"

def log(system_name, message, to_file=True):
	output = "[{}] {}: {}".format(SystemTime.get_formatted_time(), system_name, message)
	print(output)
	if to_file:
		f = open("log.txt", "a")
		f.write(output + "\n")
		f.close()
