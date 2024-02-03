from tkinter import *

def button_click(event):
    print("Button clicked!")

window = Tk()
window.title("Button Event Example")

button = Button(window, text="Click Me")
button.pack()

button.bind("<Button-1>", button_click)

window.mainloop()