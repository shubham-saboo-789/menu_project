from twilio.rest import Client

def SMSing():
	
	number = input("Enter number with the country code: ")
	message = input("Enter the message you want to send: ")
    
	account_sid = 'AC1fd7f4a2b23509026c9708d74bf82465'
	auth_token = 'fbfdf69ce5ab33e329ad1fcd7a3e7934'

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    body=message,
	    from_='+15076292590',
	    to=number
	)

	print(f"Message sent with SID: {message.sid}")

def SMSing_sch(number,message):
    
	account_sid = 'AC1fd7f4a2b23509026c9708d74bf82465'
	auth_token = 'fbfdf69ce5ab33e329ad1fcd7a3e7934'

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    body=message,
	    from_='+15076292590',
	    to=number
	)

	print(f"Message sent with SID: {message.sid}")
