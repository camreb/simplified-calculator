from buttons import *


class Calc:
    def __init__(self, root):
        self.buttons = Buttons(root).describe_interface()


root = Tk()
calc = Calc(root)
root.title("Calculator")
window_width = 350
window_height = 370
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_position_horizontal = int((screen_width / 2) - (window_width / 2))
window_position_vertical = int((screen_height / 2) - (window_height / 2))

root.geometry('{}x{}+{}+{}'.format(window_width, window_height, window_position_horizontal, window_position_vertical))
root.mainloop()
