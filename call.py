from twilio.rest import Client


def calling():
	number = input("Enter number with the country code: ")	

	account_sid = 'AC***f4a2b******26c97******f82465'
	auth_token = 'fbfdf******b33e3**********3e7934'
	
	client = Client(account_sid, auth_token)

	def make_phone_call(to_number, from_number, twiml_url):
	    call = client.calls.create(
		to=to_number,
		from_=from_number,
		url=twiml_url
	    )
	    print(f"Call Success its SID : {call.sid}")

	# Example usage
	make_phone_call(number, '+1507******0', 'http://demo.twilio.com/docs/voice.xml')

def calling_sch(number):
	# Your Account SID and Auth Token from twilio.com/console
	account_sid = 'AC1fd7f4******09026c970******82465'
	auth_token = 'fb***69ce5ab******ad1f*****7934'
	client = Client(account_sid, auth_token)

	def make_phone_call(to_number, from_number, twiml_url):
	    call = client.calls.create(
		to=to_number,
		from_=from_number,
		url=twiml_url
	    )
	    print(f"Call SID: {call.sid}")

	# Example usage
	make_phone_call(number, '+150*****590', 'http://demo.twilio.com/docs/voice.xml')
