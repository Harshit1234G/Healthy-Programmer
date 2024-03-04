from time import sleep
sleep(30)

from datetime import datetime
import pyttsx3
from win10toast import ToastNotifier

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)

notifier = ToastNotifier()

while True:
    sleep(15*60)
    notifier.show_toast("Healthy Programmer", "Take a Break!")
    print("Take Break.", datetime.now())
    engine.say("Take a break. " * 5)
    engine.runAndWait()