from time import sleep
sleep(30)

from win10toast import ToastNotifier
import pyttsx3


def notify_and_say(message: str, minutes: int) -> None:
    print(f'{minutes} minutes had passed, {message}')

    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 150)

    notifier = ToastNotifier()
    notifier.show_toast("Healthy Programmer", message)

    engine.say(message * 5)
    engine.runAndWait()


if __name__ == '__main__':
    time: int = 0

    while True:
        sleep(600)
        time += 10

        if time % 10 == 0 and time % 30 != 0:
            notify_and_say('Rest your eyes. ', time)

        elif time % 30 == 0 and time % 60 != 0:
            notify_and_say('Drink Water. ', time)

        elif time % 60 == 0:
            notify_and_say('Do some physical activity and maintain posture. ', time)
