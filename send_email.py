import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail():	
	# Email config
	smtp_server = 'smtp.gmail.com'
	smtp_port = 587
	smtp_user = 'shubhamsaboo007@gmail.com'
	smtp_password = 'zhbephdrbmifodmc'

	# Email content
	from_email = 'shubhamsaboo007@gmail.com'
	to_email =input("Enter receivers Email : ")
	subject =input("Enter Subject of your Email : ")
	body =input("Enter Body of your Email : ")

	# Ensure subject and body are encoded in UTF-8
	subject = subject.encode('utf-8').decode('utf-8')
	body = body.encode('utf-8').decode('utf-8')

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message['From'] = from_email
	message['To'] = to_email
	message['Subject'] = subject

	# Add body to email with utf-8 encoding
	message.attach(MIMEText(body, 'plain', 'utf-8'))

	try:
		# Connect to the server and send the email
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()  # Secure the connection
		server.login(smtp_user, smtp_password)
		server.sendmail(from_email, to_email, message.as_string())
		server.quit()

		print("Email sent successfully!")
	except Exception as e:
		print(f"Error: {e}")

def mail_sch(to_email,subject,body):	
	# Email configuration
	smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server
	smtp_port = 587  # Replace with your SMTP port
	smtp_user = 'shubhamsaboo007@gmail.com'  # Replace with your email address
	smtp_password = 'zhbephdrbmifodmc'  # Replace with your app password

	# Email content
	from_email = 'shubhamsaboo007@gmail.com'  # Replace with your email address
#	to_email =to_email_mail  # Replace with the recipient's email address
#	subject =sub_mail
#	body =body_mail

	# Ensure subject and body are encoded in UTF-8
	subject = subject.encode('utf-8').decode('utf-8')
	body = body.encode('utf-8').decode('utf-8')

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message['From'] = from_email
	message['To'] = to_email
	message['Subject'] = subject

	# Add body to email with utf-8 encoding
	message.attach(MIMEText(body, 'plain', 'utf-8'))

	try:
		# Connect to the server and send the email
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()  # Secure the connection
		server.login(smtp_user, smtp_password)
		server.sendmail(from_email, to_email, message.as_string())
		server.quit()

		print("Email sent successfully!")
	except Exception as e:
		print(f"Error: {e}")
	    
