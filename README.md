# Healthy Programmer
This Python script serves as a simple yet effective reminder to take breaks every 15 minutes, promoting healthy working habits. I use this script in my daily life. It utilizes:

- **time:** For scheduling notifications at specific intervals.
- **datetime:** For recording the current time when a break reminder is triggered.
- **pyttsx3:** For text-to-speech conversion, providing audio reminders.
- **win10toast:** To display visual notifications on the desktop (Windows-specific).

## Features:
- **Regular reminders:** Alerts you to take a break every 15 minutes.
- **Audio cues:** Repeats the reminder text multiple times ("Take a break.") through text-to-speech functionality.
- **Visual prompts:** Displays desktop notifications to grab your attention.
- **Time logging:** Records timestamps of triggered reminders for potential reference.

## How to use:
- Execute the script using Python.

- Set for startup (Optional):
- **Windows:**
  1. Press `Windows + r`.
  2. Type `shell:startup` and press enter.
  3. Create a shortcut of this python script in that folder.
- **Other operating systems:** Consult your specific system's documentation for setting applications to run at startup.

## Customization:
- **Time interval:** Modify the value inside `sleep(15 * 60)` to adjust the time between breaks (15 minutes by default).
- **Text-to-speech settings:** You can adjust the voice rate within the script using `engine.setProperty('rate', <desired_rate>)`. Refer to the pyttsx3 documentation for additional customization options: https://pyttsx3.readthedocs.io/
- **Toast notification settings:** Explore the win10toast documentation for customizing notification appearances: https://pypi.org/project/win10toast/

## Note:
- This script is currently designed for Windows systems due to the use of the `win10toast` library.
- Consider exploring alternative libraries for visual notifications to make the script compatible with other operating systems.

## Additional Information:
- This script is provided for educational and personal use only.
- Feel free to modify and extend it based on your specific needs and preferences.
