import schedule
import time
from datetime import datetime, timedelta
import send_email as email

def mail_scheduling():

	to_email =input("Enter your Email : ")  # Replace with the recipient's email address
	subject =input("Enter Subject of your Email : ")
	body =input("Enter Body of your Email : ")

	# Set the time you want to run the task (14:34 in this example)

	scheduled_time =input("Enter the schedule time (24:60-format) : ")

	# Calculate the delay until the scheduled time

	now = datetime.now()
	scheduled_datetime = datetime.strptime(scheduled_time, "%H:%M")
	if now > scheduled_datetime:
	    scheduled_datetime += timedelta(days=1)  # If the scheduled time has passed today, schedule it for tomorrow
	delay = (scheduled_datetime - now).total_seconds()

	# Schedule the task to run after the calculated delay
	schedule.every().seconds.do(email.mail_sch(to_email,subject,body)).tag('scheduled_task')

	# Keep the script running until the task runs
	while True:
		schedule.run_pending()
		time.sleep(1)
		if schedule.get_job('scheduled_task').next_run is None:
			break
mail_scheduling()

