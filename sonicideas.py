import tkinter as tk
from random import choice
import pyttsx3

# START DONATION CODE
from tkinter import messagebox
from random import randint
import sys


#if randint(0,3) == 1 and not "--no-popup" in sys.argv:
    #messagebox.showinfo("BirdOffice 24.11", "Thank you for downloading BirdMenu! If you like this software, make sure to donate at www.mojavesoft.net/donate/!")


# END DONATION CODE


engine = pyttsx3.init()

slime = ["peanut butter", "garlic butter", "mayo", "ketchup", "lard", "liquid gallium", "orange juice", "oil", "fart juice", "rotten denmark", "skunk juice", "moldy", "pickle", "mustard", "rancid",\
         "spoiled", "clippy", "whipped cream", "mystery meat", "smelly"]
main_course = ["sandwich", "burger", "chicken nuggets", "toilet paper", "bacon sandwich", "dead possum", "onion", "roadkill", "slushie", "potato", "earthworm"]
dessert = ["butter", "cookie", "potting soil", "bacon", "fbi agent", "cloud", "water", "mold", "cia agent", "nsa agent", "department of justice lawyer", "car salesman", "waffle", "cekukeim sauce"]

use_voice = 1

generated_foods = []

def generate_text():
    text_box.delete(1.0, tk.END)  # Clear the text box
    global generated_foods  # Access the global variable
    generated_foods = []  # Reset the list
    for _ in range(10):
        str1 = f"{choice(slime)} {choice(main_course)}, dessert is {choice(dessert)} with {choice(slime)}"
        text_box.insert(tk.END, str1 + "\n\n")
        generated_foods.append(str1)

def speak_text():
    global generated_foods  # Access the global variable
    for i in generated_foods:
        if use_voice:
            engine.say(i)
            engine.runAndWait()

# Create the main window
window = tk.Tk()
window.title("BirdMenu v24.11")
window.minsize(width=0, height=500)
# Create a text box to display the generated food combinations
text_box = tk.Text(window)
text_box.pack(expand=True, fill='both')

# Create buttons for generating text and speaking text
generate_button = tk.Button(window, text="Generate Text", command=generate_text, bg="green", fg="white")
generate_button.pack(side=tk.LEFT, expand=True, fill='both')

speak_button = tk.Button(window, text="Speak Text", command=speak_text, bg="orange")
speak_button.pack(side=tk.LEFT, expand=True, fill='both')

window.mainloop()
