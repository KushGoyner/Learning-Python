import time
import pyttsx3
import ctypes  # For Windows message box

REPEAT_INTERVAL = 10  # Repeat frequency in seconds

engine = pyttsx3.init()

def remind():
    # Text-to-speech
    engine.say("Hey Kush, drink water")
    engine.runAndWait()

    # Windows popup message
    ctypes.windll.user32.MessageBoxW(0, "Hey Kush, Drink Water!", "Reminder", 1)

while True:
    remind()
    time.sleep(REPEAT_INTERVAL)
