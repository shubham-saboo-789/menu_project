import os
import whatsapp as what
import call
import sms
import search
import send_email as email
import name_to_pic as namepic
import photo_capture
import video_capture
import delay

print("---------------MENU.PY-------------------------")
print("type 1 to whatsapp message someone")
print("type 2 to whatsapp message someone and schedule it")
print("type 3 to text message someone")
print("type 4 to text message someone and schedule it")
print("type 5 to call someone")
print("type 6 to call someone and schedule it")
print("type 7 to Google something")
print("type 8 to Email someone")
print("type 9 to Email someone and Schedule it")
print("type 10 to make a stylized picture of any text")
print("type 11 to capture a pic using IP cam and save it")
print("type 12 to capture a vid using IP cam")
print("type 13 to run a linux train")
print("type 14 to open a HTML form")
print("type 15 to open a HTML frontend for GOOGLE & BING")

print("-----------------------------------------------")

ch=input("Enter your choise : ")

if ch=='1':
	print("sending whatsapp message....")
	what.send_whatsapp()
elif ch=='2':
	print("sending whatsapp message....")
	delay.delay_send_whatsapp()
elif ch=='3':
	print("messaging the number....")
	sms.SMSing()
elif ch=='4':
	print("messaging the number....")
	delay.delay_SMSing()
elif ch=='5':
	print("calling the number....")
	call.calling()
elif ch=='6':
	print("calling the number....")
	delay.delay_calling()
elif ch=='7':
	print("Searching on Google....")
	search.search_query()
elif ch=='8':
	print("Sending the Email....")
	email.mail()
elif ch=='9':
	print("Sending the Email....")
	delay.delay_mail()
elif ch=='10':
	print("Making the pic....")
	namepic.render_letters()
elif ch=='11':
	print("Taking a pic....")
	photo_capture.click()
elif ch=='12':
	print("Taking a vid....")
	video_capture.click()
elif ch=='13':
	os.system("sl")
elif ch=='14':
	os.system("firefox data_coll.html")
elif ch=='15':
	os.system("firefox google_frontend.html")
else:
	print("invalid input try again")
	
