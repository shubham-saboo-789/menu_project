import numpy as np
import cv2

def a():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[0:100, 0:50] = [225, 225, 225]
    pic_arr[10:90, 5:15] = [0, 0, 0]
    pic_arr[10:90, 35:45] = [0, 0, 0]
    pic_arr[10:20, 5:45] = [0, 0, 0]
    pic_arr[45:55, 5:45] = [0, 0, 0]
    return pic_arr
def b():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]  # Set the entire image to white
    pic_arr[10:90, 5:15] = [0, 0, 0]  # Left vertical line
    pic_arr[10:30, 15:40] = [0, 0, 0]  # Top horizontal bar
    pic_arr[40:60, 15:40] = [0, 0, 0]  # Middle horizontal bar
    pic_arr[70:90, 15:40] = [0, 0, 0]  # Bottom horizontal bar
    pic_arr[30:40, 35:40] = [0, 0, 0]  # Middle vertical bar
    pic_arr[60:70, 35:40] = [0, 0, 0]  # Lower vertical bar
    return pic_arr
def c():
    pic_arr = numpy.zeros((100, 50, 3), dtype=numpy.uint8)
    pic_arr[10:90, 5:15] = [255, 255, 255]  # Vertical bar of 'C'
    pic_arr[10:20, 15:45] = [255, 255, 255]  # Horizontal| top bar of 'C'
    pic_arr[80:90, 15:45] = [255, 255, 255]  # Horizontal bottom bar of 'C' 
    return pic_arr
def d():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]  # Set the entire image to white
    pic_arr[10:90, 5:15] = [0, 0, 0]  # Left vertical bar of 'D'
    pic_arr[10:20, 5:40] = [0, 0, 0]  # Top horizontal bar of 'D'
    pic_arr[80:90, 5:40] = [0, 0, 0]  # Bottom horizontal bar of
    pic_arr[20:30, 30:40] = [0, 0, 0]  # Upper right vertical bar of 'D'
    pic_arr[70:80, 30:40] = [0, 0, 0]  # Lower right vertical bar of 'D'
    pic_arr[30:70, 35:45] = [0, 0, 0]  # Middle right vertical bar of 'D'
    return pic_arr
def e():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]  # Set the entire image to white
    pic_arr[10:90, 5:15] = [0, 0, 0]  # Left vertical bar of 'E'
    pic_arr[10:20, 5:45] = [0, 0, 0]  # Top horizontal bar of 'E'
    pic_arr[45:55, 5:35] = [0, 0, 0]  # Middle horizontal bar of 'E'
    pic_arr[80:90, 5:45] = [0, 0, 0]  # Bottom horizontal bar of 'E'
    return pic_arr
def f():
    pic_arr = numpy.zeros((100, 50, 3), dtype=numpy.uint8)
    pic_arr[10:90, 5:15] = [225, 225, 225]  # Vertical bar of 'C'
    pic_arr[10:20, 15:45] = [225, 225, 225]  # Horizontal bar of 'C'
    pic_arr[45:55, 15:45] = [225, 225, 225]  # Horizontal bar of 'C'
    return pic_arr
def g():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]
    pic_arr[10:90, 5:15] = [0, 0, 0]
    pic_arr[10:20, 5:45] = [0, 0, 0]
    pic_arr[80:90, 5:45] = [0, 0, 0]
    pic_arr[45:55, 25:45] = [0, 0, 0]
    pic_arr[45:55, 35:45] = [0, 0, 0]
    pic_arr[55:80, 35:45] = [0, 0, 0]
    pic_arr[70:80, 25:35] = [0, 0, 0]
    return pic_arr
def h():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[10:90, 10:20] = [225, 225, 225]  # Left vertical bar of 'H'
    pic_arr[10:90, 30:40] = [225, 225, 225]  # Right vertical bar of 'H'
    pic_arr[40:50, 10:40] = [225, 225, 225]  # Horizontal bar of 'H'
    return pic_arr
def i():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]
    pic_arr[10:90, 20:30] = [0, 0, 0]
    pic_arr[10:20, 5:45] = [0, 0, 0]
    pic_arr[80:90, 5:45] = [0, 0, 0]
    return pic_arr
def j():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]
    pic_arr[10:20, 5:45] = [0, 0, 0]
    pic_arr[10:90, 30:40] = [0, 0, 0]
    pic_arr[80:90, 5:35] = [0, 0, 0]
    pic_arr[70:80, 5:15] = [0, 0, 0]
    return pic_arr
def k():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]
    pic_arr[10:90, 5:15] = [0, 0, 0]
    pic_arr[45:55, 15:25] = [0, 0, 0]
    pic_arr[35:45, 25:35] = [0, 0, 0]
    pic_arr[25:35, 35:45] = [0, 0, 0]
    pic_arr[55:65, 25:35] = [0, 0, 0]
    pic_arr[65:75, 35:45] = [0, 0, 0]
    return pic_arr
def l():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]
    pic_arr[10:90, 5:15] = [0, 0, 0]
    pic_arr[80:90, 5:45] = [0, 0, 0]
    return pic_arr
def m():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[10:90, 5:15] = [225, 225, 225]  # Left vertical bar of 'M'
    pic_arr[10:90, 35:45] = [225, 225, 225]  # Right vertical bar of 'M'
    pic_arr[10:30, 15:25] = [225, 225, 225]  # Left diagonal bar of 'M'
    pic_arr[10:30, 25:35] = [225, 225, 225]  # Right diagonal bar of 'M'
    pic_arr[30:50, 20:30] = [225, 225, 225]  # Middle vertical bar of 'M'
    return pic_arr
def n():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]
    pic_arr[10:90, 5:15] = [0, 0, 0]    # Left vertical bar of 'N'
    pic_arr[10:90, 35:45] = [0, 0, 0]   # Right vertical bar of 'N'
    pic_arr[10:20, 15:25] = [0, 0, 0]
    pic_arr[20:30, 20:30] = [0, 0, 0]
    pic_arr[30:40, 25:35] = [0, 0, 0]
    pic_arr[40:50, 30:40] = [0, 0, 0]
    pic_arr[50:60, 35:45] = [0, 0, 0]
    return pic_arr
def o():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]
    pic_arr[10:90, 5:15] = [0, 0, 0]  # Left vertical bar of 'O'
    pic_arr[10:90, 35:45] = [0, 0, 0]  # Right vertical bar of 'O'
    pic_arr[10:20, 5:45] = [0, 0, 0]  # Top horizontal bar of 'O'
    pic_arr[80:90, 5:45] = [0, 0, 0]  # Bottom horizontal bar of 'O'
    return pic_arr
def p():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]
    pic_arr[10:90, 5:15] = [0, 0, 0]  # Left vertical bar of 'P'
    pic_arr[10:20, 5:40] = [0, 0, 0]  # Top horizontal bar of 'P'
    pic_arr[45:55, 5:40] = [0, 0, 0]  # Middle horizontal bar of 'P'
    pic_arr[20:45, 35:45] = [0, 0, 0]  # Right vertical bar of 'P'
    return pic_arr
def q():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [0, 0, 0]  # Set the entire image to black
    pic_arr[10:90, 5:15] = [225, 225, 225]  # Left vertical bar of 'Q'
    pic_arr[10:90, 35:45] = [225, 225, 225]  # Right vertical bar of 'Q'
    pic_arr[10:20, 5:45] = [225, 225, 225]  # Top horizontal bar of 'Q'
    pic_arr[80:90, 5:45] = [225, 225, 225]  # Bottom horizontal bar of 'Q'
    pic_arr[70:90, 25:35] = [225, 225, 225]  # Diagonal line of 'Q'
    return pic_arr
def r():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [0, 0, 0]  # Set the entire image to black
    pic_arr[10:90, 5:15] = [225, 225, 225]  # Left vertical bar of 'R'
    pic_arr[10:20, 5:45] = [225, 225, 225]  # Top horizontal bar of 'R'
    pic_arr[45:55, 5:40] = [225, 225, 225]  # Middle horizontal bar of 'R'
    pic_arr[20:45, 35:45] = [225, 225, 225]  # Right vertical bar of 'R'
    pic_arr[55:90, 35:45] = [225, 225, 225]  # Right diagonal line of 'R'
    return pic_arr
def s():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[10:20, 10:40] = [225, 225, 225]   # Top horizontal bar of 'S'
    pic_arr[40:50, 10:40] = [225, 225, 225]   # Middle horizontal bar of 'S'
    pic_arr[70:80, 10:40] = [225, 225, 225]   # Bottom horizontal bar of 'S'
    pic_arr[20:40, 10:20] = [225, 225, 225]   # Top-left vertical bar of 'S'
    pic_arr[50:70, 30:40] = [225, 225, 225]   # Bottom-right vertical bar of 'S'
    return pic_arr
def t():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]  # Set the entire image to white
    pic_arr[10:20, 5:45] = [0, 0, 0]  # Top horizontal bar of 'T'
    pic_arr[10:90, 20:30] = [0, 0, 0]  # Middle vertical bar of 'T'
    return pic_arr
def u():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[10:90, 10:20] = [225, 225, 225]  # Left vertical bar of 'U'
    pic_arr[10:90, 30:40] = [225, 225, 225]  # Right vertical bar of 'U'
    pic_arr[80:90, 10:40] = [225, 225, 225]  # Bottom horizontal bar of 'U'
    return pic_arr
def v():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [0, 0, 0]  # Set the entire image to black
    pic_arr[10:30, 5:15] = [225, 225, 225]  # Top left box of 'V'
    pic_arr[10:30, 35:45] = [225, 225, 225]  # Top right box of 'V'
    pic_arr[30:50, 10:20] = [225, 225, 225]  # Middle left box of 'V'
    pic_arr[30:50, 30:40] = [225, 225, 225]  # Middle right box of 'V'
    pic_arr[50:70, 20:30] = [225, 225, 225]  # Bottom box of 'V'
    return pic_arr
def w():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [0, 0, 0]  # Set the entire image to black
    pic_arr[10:70, 5:15] = [225, 225, 225]  # Left vertical bar of 'W'
    pic_arr[10:70, 35:45] = [225, 225, 225]  # Right vertical bar of 'W'
    pic_arr[50:70, 15:25] = [225, 225, 225]  # Middle left diagonal bar of 'W'
    pic_arr[50:70, 25:35] = [225, 225, 225]  # Middle right diagonal bar of 'W'
    pic_arr[70:90, 10:20] = [225, 225, 225]  # Bottom left bar of 'W'
    pic_arr[70:90, 30:40] = [225, 225, 225]  # Bottom right bar of 'W'
    return pic_arr
def x():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [0, 0, 0]  # Set the entire
    pic_arr[10:30, 10:20] = [225, 225, 225]
    pic_arr[30:50, 20:30] = [225, 225, 225]
    pic_arr[50:70, 30:40] = [225, 225, 225]
    pic_arr[70:90, 40:50] = [225, 225, 225]
    pic_arr[10:30, 30:40] = [225, 225, 225]
    pic_arr[30:50, 20:30] = [225, 225, 225]
    pic_arr[50:70, 10:20] = [225, 225, 225]
    pic_arr[70:90, 0:10] = [225, 225, 225]
    return pic_arr
def y():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [225, 225, 225]  # Set the entire image to white
    pic_arr[10:40, 10:20] = [0, 0, 0]  # Left diagonal line of 'V'
    pic_arr[10:40, 30:40] = [0, 0, 0]  # Right diagonal line of 'V'
    pic_arr[40:90, 20:30] = [0, 0, 0]  # Center vertical bar of 'V'
    return pic_arr
def z():
    pic_arr = np.zeros((100, 50, 3), dtype=np.uint8)
    pic_arr[:] = [0, 0, 0]
    thickness = 7  # Set the thickness of the lines
    cv2.line(pic_arr, (5, 10), (45, 10), (255, 255, 255), thickness)
    cv2.line(pic_arr, (5, 90), (45, 90), (255, 255, 255), thickness)
    cv2.line(pic_arr, (45, 10), (5, 90), (255, 255, 255), thickness)
    return pic_arr


def render_letters():
	name =input("Enter someting that you want to make a pic of : ")
	length=len(name)
	start = 0
	end = 50

	pic_arr = np.zeros((100, 50 * length, 3), dtype=np.uint8)
	add_arr = np.zeros((100, 50, 3), dtype=np.uint8)

	for char in name:
		if char == 'a':
			add_arr = a()
		elif char == 'b':
			add_arr = b()
		elif char == 'c':
			add_arr = c()
		elif char == 'd':
			add_arr = d()
		elif char == 'e':
			add_arr = e()
		elif char == 'f':
			add_arr = f()
		elif char == 'g':
			add_arr = g()
		elif char == 'h':
			add_arr = h()
		elif char == 'i':
			add_arr = i()
		elif char == 'j':
			add_arr = j()
		elif char == 'k':
			add_arr = k()
		elif char == 'l':
			add_arr = l()
		elif char == 'm':
			add_arr = m()
		elif char == 'n':
			add_arr = n()
		elif char == 'o':
			add_arr = o()
		elif char == 'p':
			add_arr = p()
		elif char == 'q':
			add_arr = q()
		elif char == 'r':
			add_arr = r()
		elif char == 's':
			add_arr = s()
		elif char == 't':
			add_arr = t()
		elif char == 'u':
			add_arr = u()
		elif char == 'v':
			add_arr = v()
		elif char == 'w':
			add_arr = w()
		elif char == 'x':
			add_arr = x()
		elif char == 'y':
			add_arr = y()
		elif char == 'z':
			add_arr = z()
		elif char ==' ':
			add_arr[:]=[225,225,255]
		else:
			add_arr[:]=[225,225,255]
		
		pic_arr[0:100, start:end] = add_arr
		start += 50
		end += 50

		cv2.imshow("Letters", pic_arr)
		cv2.waitKey(5000)
		cv2.destroyAllWindows()

