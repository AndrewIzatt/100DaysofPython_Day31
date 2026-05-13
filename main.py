from tkinter import *
from tkinter import PhotoImage
import pandas
import random

from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
FONT_NAME = "Ariel"
FIRST_LANGUAGE = "English"
SECOND_LANGUAGE = "Spanish"
foreign_word = None
target_word = None

try:
    data = pandas.read_csv("data/unknown_words_english.csv")
except pandas.errors.EmptyDataError:
    print("You have no more words to learn!")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words_small.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def generate_card_front():
    global current_word
    try:
        print(f"inside generate_card_front - current_word: {current_word}")
    except NameError:
        print(f"inside generate_card_front - current_word is empty")
    global FLIP_TIMER
    print(f"inside generate_card_front - FLIP_TIMER: {FLIP_TIMER}")
    window.after_cancel(FLIP_TIMER)
    try:
        current_word = random.choice(to_learn)
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(top_text, text=FIRST_LANGUAGE, fill="black")
        canvas.itemconfig(bottom_text, text=current_word[FIRST_LANGUAGE], fill="black")
    except IndexError:
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(top_text, text="Congratulations!", fill="black")
        canvas.itemconfig(bottom_text, text="You know all the words!", fill="black")

    FLIP_TIMER = window.after(3000, generate_card_back)


def generate_card_back():
    print(f"inside generate_card_back - current_word: {current_word}")
    print(f"inside generate_card_back - FLIP_TIMER: {FLIP_TIMER}")
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(top_text, text=SECOND_LANGUAGE, fill="white")
    canvas.itemconfig(bottom_text, text=current_word[SECOND_LANGUAGE], fill="white")


def known_card_old():
    # Don't Use - My original attempt
    global to_learn
    global current_word
    print(f"len of current_word {len(current_word)}")
    if len(current_word) > 0:
        print(f"current_word: {current_word}")
        for word in to_learn:
            if word[FIRST_LANGUAGE] == current_word[FIRST_LANGUAGE]:
                to_learn.remove(word)
                updated_to_learn = pandas.DataFrame(to_learn)
                updated_to_learn.to_csv("data/known_words_english.csv", index=False)
    print(f"to_learn: {to_learn}")
    print("Generating card:")
    generate_card_front()

def known_card():
    print(f"inside known_card - current_word: {current_word}")
    print(f"inside known_card - FLIP_TIMER: {FLIP_TIMER}")
    to_learn.remove(current_word)
    updated_to_learn = pandas.DataFrame(to_learn)
    updated_to_learn.to_csv("data/known_words_english.csv", index=False)
    print("Generating card:")
    generate_card_front()

# Initiate window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

FLIP_TIMER = window.after(3000, generate_card_back)

#Flash Card
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
top_text = canvas.create_text(400, 150, text=FIRST_LANGUAGE, fill="black", font=(FONT_NAME, 40, "italic"))
bottom_text = canvas.create_text(400, 263, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=known_card)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=generate_card_front)
unknown_button.grid(row=1, column=0)

generate_card_front()

# print(f"Next to mainloop - current_word: {current_word}")
print(f"Next to mainloop - FLIP_TIMER: {FLIP_TIMER}")
window.mainloop()