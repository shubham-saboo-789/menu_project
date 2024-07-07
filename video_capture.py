import cv2

def click():
	ip=input("Enter the IP cam's IP : ")
	cap_ip=cv2.VideoCapture("http://"+ip+"/video")
	while True:
		status_ip,photo_ip=cap_ip.read()
		cv2.imshow("photo_ip",photo_ip)
		if cv2.waitKey(100)==13:
			break
	cv2.destroyAllWindows()
	cap_ip.release()
