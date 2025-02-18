# Time to rest your eyes

A Python script designed to help reduce eye strain by reminding you to rest your eyes for one minute every 15 minutes. It achieves this by displaying an image as a popup at random screen locations, ensuring you take a break from the screen. The popup remains visible for one minute and cannot be closed manually, disappearing automatically once the time is up.


## Installation, Usage & Configuration

1. Install Python.

2. Install the required dependency:

```
pip install pillow

```

3. The script comes with a default image file named `timer.jpeg`, which will be used for the popup. You can either use this image or modify the `img_path` variable in the script to specify another image.

4. Run the script:

```
python mytimer.py

```

5. The program will:

   - Wait 15 minutes.

   - Display an image popup that cannot be closed manually.

   - Keep the image visible for one minute before closing.

   - Repeat the cycle indefinitely.


## Customization

You can adjust the following variables in the script:

- timer = 15 * 60 → Sets the time interval between breaks (default: 15 minutes).

- rest_time = 60000 → Determines how long the popup stays open (default: 1 minute, in milliseconds).

- img_path = "timer.jpeg" → Specifies the image file to be displayed.

## Stopping the Script

To stop the script, close the terminal or press Ctrl + C.
