from tkinter import Button, StringVar, Entry
from calculator.math_logic import MathLogic


class Buttons:

    def __init__(self, root):
        self.root = root

        # Define Entry Box
        # Following e.get, e.insert, e.delete commands refer to Entry Box
        default_value = StringVar(self.root, value="0")
        self.entry_box = Entry(self.root, width=40, textvariable=default_value)

        # Put Entry Box on the screen
        self.entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        operation = MathLogic(self.entry_box)

        # Define buttons
        def button(number: str):
            return Button(self.root, text=number, padx=35, pady=15, command=lambda: operation.click(number))

        number_button = (button('1'), button('2'), button('3'), button('4'), button('5'), button('6'), button('7'),
                         button('8'), button('9'), button('0'))
        self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7, \
        self.button_8, self.button_9, self.button_0 = number_button

        self.button_add = Button(self.root, text='+', padx=34, pady=15, command=operation.button_add)
        self.button_subtract = Button(self.root, text='-', padx=36, pady=15, command=operation.button_subtract)
        self.button_multiply = Button(self.root, text='*', padx=36, pady=15, command=operation.button_multiply)
        self.button_divide = Button(self.root, text='/', padx=36, pady=15, command=operation.button_divide)
        self.button_opposite = Button(self.root, text='+/-', padx=29, pady=15, command=operation.opposite)
        self.button_equal = Button(self.root, text='=', padx=34, pady=15, command=operation.equal)
        self.button_clear = Button(self.root, text='C', padx=35, pady=15, command=operation.clear)
        self.button_clearentry = Button(self.root, text='CE', padx=32, pady=15, command=operation.clearentry)
        self.button_comma = Button(self.root, text='.', padx=37, pady=15, command=lambda: operation.click("."))

        self.button_backspace = Button(self.root, text='<--', padx=29, pady=15, command=operation.backspace)
        self.button_inverse = Button(self.root, text='1/x', padx=29, pady=15, command=operation.inverse)
        self.button_sqr = Button(self.root, text='x²', padx=33, pady=15, command=operation.sqr)
        self.button_sqrt = Button(self.root, text='√x', padx=32, pady=15, command=operation.sqrt)
        self.button_percent = Button(self.root, text='%', padx=33, pady=15, command=operation.percent)

    # Put buttons on the screen
    def describe_interface(self):
        self.button_1.grid(row=5, column=0)
        self.button_2.grid(row=5, column=1)
        self.button_3.grid(row=5, column=2)
        self.button_4.grid(row=4, column=0)
        self.button_5.grid(row=4, column=1)
        self.button_6.grid(row=4, column=2)
        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)
        self.button_0.grid(row=6, column=1)

        self.button_add.grid(row=5, column=3)
        self.button_subtract.grid(row=4, column=3)
        self.button_multiply.grid(row=3, column=3)
        self.button_divide.grid(row=2, column=3)
        self.button_opposite.grid(row=6, column=0)
        self.button_comma.grid(row=6, column=2)
        self.button_equal.grid(row=6, column=3)

        self.button_percent.grid(row=1, column=0)
        self.button_clearentry.grid(row=1, column=1)
        self.button_clear.grid(row=1, column=2)
        self.button_backspace.grid(row=1, column=3)
        self.button_inverse.grid(row=2, column=0)
        self.button_sqr.grid(row=2, column=1)
        self.button_sqrt.grid(row=2, column=2)
