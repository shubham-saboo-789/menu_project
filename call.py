from twilio.rest import Client


def calling():
	number = input("Enter number with the country code: ")	

	account_sid = 'AC1fd7f4a2b23509026c9708d74bf82465'
	auth_token = 'fbfdf69ce5ab33e329ad1fcd7a3e7934'
	
	client = Client(account_sid, auth_token)

	def make_phone_call(to_number, from_number, twiml_url):
	    call = client.calls.create(
		to=to_number,
		from_=from_number,
		url=twiml_url
	    )
	    print(f"Call Success its SID : {call.sid}")

	# Example usage
	make_phone_call(number, '+15076292590', 'http://demo.twilio.com/docs/voice.xml')

def calling_sch(number):
	# Your Account SID and Auth Token from twilio.com/console
	account_sid = 'AC1fd7f4a2b23509026c9708d74bf82465'
	auth_token = 'fbfdf69ce5ab33e329ad1fcd7a3e7934'
	client = Client(account_sid, auth_token)

	def make_phone_call(to_number, from_number, twiml_url):
	    call = client.calls.create(
		to=to_number,
		from_=from_number,
		url=twiml_url
	    )
	    print(f"Call SID: {call.sid}")

	# Example usage
	make_phone_call(number, '+15076292590', 'http://demo.twilio.com/docs/voice.xml')
