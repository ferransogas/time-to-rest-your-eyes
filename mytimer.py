import time
import tkinter as tk
from PIL import Image, ImageTk
import random

def update_position(root):
    x, y = random.randint(0, root.winfo_screenwidth() - 140), random.randint(0, root.winfo_screenheight() - 70)
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}+{x}+{y}')

def open_img():

    # Create a window with no decorations
    root = tk.Tk()
    root.overrideredirect(1)
    # Set the window to be transparent
    root.attributes('-alpha', 1.0)
    #root.attributes('-topmost', True)
    root.wm_attributes('-transparentcolor', root.cget('bg'))
    # Load an image and preserve its aspect ratio
    path = "hola.jpg"
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
    
    root.after(1000, update_position(root))
    
    
    # Start the event loop
    root.after(90000, root.destroy)
    root.mainloop()

while(1):
    time.sleep(3)
    open_img()