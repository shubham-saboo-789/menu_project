import time
import send_email
import sms
import call
import whatsapp

def delay_sec():
	sec=int(input("Enter the Delay (in sec) : "))
	time.sleep(sec)
	print("Delay has ended")


def delay_mail():
	to_email =input("Enter receivers Email : ")  # Replace with the recipient's email address
	subject =input("Enter Subject of your Email : ")
	body =input("Enter Body of your Email : ")
	delay_sec()
	send_email.mail_sch(to_email,subject,body)
	
def delay_sms():
	number = input("Enter number with the country code: ")
	message = input("Enter the message you want to send: ")
	delay_sec()
	sms.SMSing_sch(number,message)

def delay_calling():
	number = input("Enter number with the country code: ")
	delay_sec()
	call.calling_sch(number)

def delay_send_whatsapp():
	number = input("Enter number with the country code: ")
	message = input("Enter the message you want to send: ")
	delay_sec()
	whatsapp.send_whatsapp_sch(number,message)
