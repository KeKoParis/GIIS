from tkinter import *
from tkinter import ttk

import sys

from loguru import logger

from lines import DDA

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add("out.log")

"""
window layout
"""
window = Tk()
window.title("Graphical Editor")
window.geometry("800x620")

"""
canvas layout
"""
canvas = Canvas(window, width=800, height=500, background="white")
canvas.grid(row=0, column=0)

clear_canvas_button = Button(window, text="Clear")
clear_canvas_button.grid(row=3, column=0)

"""
action radiobutton frame
"""

selected_option = StringVar(value="line")

radiobutton_frame = Frame(window)
radiobutton_frame.grid(row=1, column=0)

line_radiobutton = Radiobutton(radiobutton_frame, variable=selected_option, text="Line", value="line")
circle_radiobutton = Radiobutton(radiobutton_frame, variable=selected_option, text="Circle", value="circle")

circle_radiobutton.grid(row=0, column=1)
line_radiobutton.grid(row=0, column=0)

"""
figure frame
"""

figure_frame = Frame(window)
figure_frame.grid(row=2, column=0)

"""
lines menu layout
"""
line_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
line_frame.grid(row=0, column=0, padx=2, pady=2)

line_label = Label(line_frame, text="Lines", font="Arial")
line_label.grid()

algorithms = ["DDA", "Bresenham", "Wu's line algorithm"]
line_box = ttk.Combobox(line_frame, values=algorithms, state="readonly")
line_box.current(0)
line_box.grid()

"""
circles layout
"""

# circle_frame = Frame(figure_frame, highlightbackground="black", highlightthickness=1)
# circle_frame.grid(row=0, column=1, padx=2, pady=2)
#
# circle_label = Label(circle_frame, text="Circles", font='Arial')
# circle_label.grid()
#
# circle_box = ttk.Combobox(circle_frame, values=algorithms, state="readonly")
# circle_box.current(0)
# circle_box.grid()


"""
events
"""

draw = list()


def figure_click(event):
    """
    Click to draw line.
    """
    logger.debug(f"radio button option: {selected_option.get()}; line algorithm: {line_box.get()}")
    logger.debug(event)

    if len(draw) == 0:
        draw.append(event)
    else:
        if draw[0].x == event.x and draw[0].y == event.y:
            return

        draw.append(event)
        points = DDA.DDA(draw[0], draw[1])

        print(points)
        for i in points:
            canvas.create_oval(i[0], i[1], i[0] + 1, i[1] + 1, fill="black")

        draw.clear()


def clear_canvas(event):
    """
    Clear canvas function
    """
    logger.debug("now canvas is clear")
    canvas.delete("all")


"""
event bindings
"""
canvas.bind("<Button-1>", figure_click)
clear_canvas_button.bind("<Button-1>", clear_canvas)

window.mainloop()
