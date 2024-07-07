import cv2
import numpy as np

def click():
#	ip="192.168.15.118:8080"
	ip=input("Enter the IP cam's IP : ")
	cap2 = cv2.VideoCapture("http://"+ip+"/video")

	if not cap2.isOpened():
		print("Error: Could not open camera.")
	else:
		status, photo = cap2.read()	    
		if status:
			cv2.imshow("shubham2", photo)
			cv2.waitKey(5000)  # Wait for 2 seconds
			save_ch=input("Do you want to save this photo [y/n]")
			if save_ch=='y':
				save_name=input("Enter name of the pic (without extention) :")
				cv2.imwrite(save_name+".jpg", photo)
			else:
				print("pic not saved")
		else:
			print("Error: Could not read frame.")	    
		cap2.release()
		
			
		cv2.destroyAllWindows()

