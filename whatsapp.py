import pywhatkit
import pyautogui
import time

def send_whatsapp():
    number = input("Enter number with the country code: ")
    message = input("Enter the message you want to send: ")

    # Send the message to WhatsApp Web
    pywhatkit.sendwhatmsg_instantly(number, message, wait_time=30, tab_close=True, close_time=30)

    # Wait for a short time to ensure the message is typed
    time.sleep(10)

    # Simulate pressing Enter to send the message
    pyautogui.press('enter')

#send_whatsapp()
def send_whatsapp_sch(number,message):

    # Send the message to WhatsApp Web
    pywhatkit.sendwhatmsg_instantly(number, message, wait_time=30, tab_close=True, close_time=30)

    # Wait for a short time to ensure the message is typed
    time.sleep(10)

    # Simulate pressing Enter to send the message
    pyautogui.press('enter')
