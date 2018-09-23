from bikeshare import SystemTime
__name__ = "Logger"

on = True

def log(system_name, message, to_file=True):
	if not on:
		return
	output = "[{}] {}: {}".format(SystemTime.get_formatted_time(), system_name, message)
	print(output)
	if to_file:
		f = open("log.txt", "a")
		f.write(output + "\n")
		f.close()
