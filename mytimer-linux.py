import time
import tkinter as tk
from PIL import Image, ImageTk
import random

img_path="timer.jpeg"
timer=15*60     #min*60sec = 15min
rest_time=60000 #min*60sec*1000ms = 1min

def open_img():

    # Create a window with no decorations
    root = tk.Tk()
    root.overrideredirect(1)
    # Set the window to be transparent
    root.attributes('-alpha', 0.5)  # Adjust transparency as needed
    root.wm_attributes('-type', 'splash')  # This line keeps the window on top
    # Load an image and preserve its aspect ratio
    path = img_path
    image = Image.open(path)
    original_size = image.size
    width, height = image.size
    if width > height:
        ratio = 300 / width
    else:
        ratio = 300 / height
    resized_image = image.resize((int(width * ratio), int(height * ratio)))
    photo = ImageTk.PhotoImage(resized_image)
    # Create a label to display the image
    label = tk.Label(root, image=photo)
    label.pack()
    
    # Set the window position to a random point on the screen
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = random.randint(0, screen_width - root.winfo_width())
    y = random.randint(0, screen_height - root.winfo_height())
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}+{x}+{y}')
    

    # Start the event loop
    root.after(rest_time, root.destroy)
    root.mainloop()

while(1):
    time.sleep(timer)
    open_img()
