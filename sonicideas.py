import tkinter as tk
from random import choice
import pyttsx3

engine = pyttsx3.init()

slime = ["peanut butter", "garlic butter", "mayo", "ketchup", "lard", "liquid gallium", "orange juice", "oil", "fart juice", "rotten denmark", "skunk juice", "moldy", "pickle", "mustard", "rancid",\
         "spoiled"]
main_course = ["sandwich", "burger", "chicken nuggets", "toilet paper", "bacon sandwich", "dead possum", "onion", "roadkill", "slushie"]
dessert = ["butter", "cookie", "potting soil", "bacon", "fbi agent", "cloud", "water", "mold", "cia agent", "nsa agent", "department of justice lawyer"]

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
window.title("BirdMenu v1.0")

# Create a text box to display the generated food combinations
text_box = tk.Text(window)
text_box.pack(expand=True, fill='both')

# Create buttons for generating text and speaking text
generate_button = tk.Button(window, text="Generate Text", command=generate_text)
generate_button.pack(side=tk.LEFT, expand=True, fill='both')

speak_button = tk.Button(window, text="Speak Text", command=speak_text)
speak_button.pack(side=tk.LEFT, expand=True, fill='both')

window.mainloop()
