from tkinter import *
from tkinter import PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

# Initiate window
window = Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Flash Card
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="/Users/meno/Repos/100DaysofPython_Day31/images/card_front.png")
canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="/Users/meno/Repos/100DaysofPython_Day31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, relief=FLAT)
right_button.grid(row=1, column=1)
wrong_image = PhotoImage(file="/Users/meno/Repos/100DaysofPython_Day31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, relief=FLAT)
wrong_button.grid(row=1, column=0)

window.mainloop()