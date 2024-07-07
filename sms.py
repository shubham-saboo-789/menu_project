from twilio.rest import Client

def SMSing():
	
	number = input("Enter number with the country code: ")
	message = input("Enter the message you want to send: ")
    
	account_sid = 'AC1fd7f4a*******026c9708d******465'
	auth_token = 'f***f69ce********9ad1fcd7****934'

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    body=message,
	    from_='+150******90',
	    to=number
	)

	print(f"Message sent with SID: {message.sid}")

def SMSing_sch(number,message):
    
	account_sid = 'A***d7f4a2b********c9708d7******65'
	auth_token = 'fbf***9c****33e329a********e7934'

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    body=message,
	    from_='+15******590',
	    to=number
	)

	print(f"Message sent with SID: {message.sid}")
