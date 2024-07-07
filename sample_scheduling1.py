import time
from datetime import datetime

def run_at_specific_time(target_time):
	target_hour, target_minute = map(int, target_time.split(":"))

	while True:
		now = datetime.now()
		current_hour = now.hour
		current_minute = now.minute
		current_second = now.second

		if current_hour == target_hour and current_minute == target_minute:
			if current_second == 0:
				my_function()
				break

		time.sleep(1)

def my_function():
	print("The specified time has arrived! Running the function...")

target_time = input("Enter the time to run the function (HH:MM): ")
run_at_specific_time(target_time)
