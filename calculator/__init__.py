from calculator.buttons import *
from tkinter import Tk


def create_calculator(calc_name: str):
    root = Tk()
    root.title(calc_name)

    Buttons(root).describe_interface()

    window_width = 350
    window_height = 370
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_position_horizontal = int((screen_width / 2) - (window_width / 2))
    window_position_vertical = int((screen_height / 2) - (window_height / 2))

    root.geometry(f'{window_width}x{window_height}+{window_position_horizontal}+{window_position_vertical}')
    root.mainloop()

