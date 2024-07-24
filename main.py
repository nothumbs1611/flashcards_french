from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# import data
words = pandas.read_csv("french_words.csv")
to_learn = words.to_dict(orient="records")
current_card = {}
# pick random word from the csv, put it into the fields
def select_word():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text  = "French", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
#create flashcard
window = Tk()
window.title("flashcard game")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

#pause 3 seconds, then flip the card
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=front_card)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# add labels
card_title = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# add buttons
wrong_image = PhotoImage(file="wrong.png")
unknown_button = Button(image = wrong_image, highlightthickness=0, command=select_word)
unknown_button.grid(row = 1, column = 0)

right_image = PhotoImage(file="right.png")
known_button = Button(image=right_image, highlightthickness=0, command=select_word)
known_button.grid(row=1, column=1)

select_word()

# when selecting either button, generate a new random word


window.mainloop()
