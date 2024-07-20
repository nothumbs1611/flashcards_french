from tkinter import *



BACKGROUND_COLOR = "#B1DDC6"

#create flashcard
window = Tk()
window.title("flashcard game")
canvas = Canvas(width=850, height=750, bg=BACKGROUND_COLOR, highlightthickness = 0)
front_card = PhotoImage(file="card_front.png")
canvas.create_image(430, 300, image=front_card)
window.config(padx=50, pady=50)
canvas.grid(row=0, column=0, columnspan = 2)

# make labels
lang_label = Label(text="French", font = ("Ariel", 40, "italic"))
lang_label.place(x = 325,y = 250)

# make buttons
keep_image = PhotoImage(file="wrong.png")
keep_button = Button(image=keep_image, highlightthickness=0)
keep_button.grid(row=0, column = 0)

window.mainloop()