from tkinter import *
from math_logic import Calculator


class Buttons:

    def __init__(self, root):
        self.root = root

    def describe_interface(self):
        # Define Entry Box
        # Following e.get, e.insert, e.delete commands refer to Entry Box
        default_value = StringVar(self.root, value="0")
        entry_box = Entry(self.root, width=40, textvariable=default_value)
        # Put Entry Box on the screen
        entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        operation = Calculator(entry_box)

        # Define buttons
        button_1 = Button(self.root, text='1', padx=35, pady=15, command=lambda: operation.click("1"))
        button_2 = Button(self.root, text='2', padx=35, pady=15, command=lambda: operation.click("2"))
        button_3 = Button(self.root, text='3', padx=35, pady=15, command=lambda: operation.click("3"))
        button_4 = Button(self.root, text='4', padx=35, pady=15, command=lambda: operation.click("4"))
        button_5 = Button(self.root, text='5', padx=35, pady=15, command=lambda: operation.click("5"))
        button_6 = Button(self.root, text='6', padx=35, pady=15, command=lambda: operation.click("6"))
        button_7 = Button(self.root, text='7', padx=35, pady=15, command=lambda: operation.click("7"))
        button_8 = Button(self.root, text='8', padx=35, pady=15, command=lambda: operation.click("8"))
        button_9 = Button(self.root, text='9', padx=35, pady=15, command=lambda: operation.click("9"))
        button_0 = Button(self.root, text='0', padx=35, pady=15, command=lambda: operation.click("0"))

        button_add = Button(self.root, text='+', padx=34, pady=15, command=operation.button_add)
        button_subtract = Button(self.root, text='-', padx=36, pady=15, command=operation.button_subtract)
        button_multiply = Button(self.root, text='*', padx=36, pady=15, command=operation.button_multiply)
        button_divide = Button(self.root, text='/', padx=36, pady=15, command=operation.button_divide)
        button_opposite = Button(self.root, text='+/-', padx=29, pady=15, command=operation.opposite)
        button_equal = Button(self.root, text='=', padx=34, pady=15, command=operation.equal)
        button_clear = Button(self.root, text='C', padx=35, pady=15, command=operation.clear)
        button_clearentry = Button(self.root, text='CE', padx=32, pady=15, command=operation.clearentry)
        button_comma = Button(self.root, text='.', padx=37, pady=15, command=lambda: operation.click("."))

        button_backspace = Button(self.root, text='<--', padx=29, pady=15, command=operation.backspace)
        button_inverse = Button(self.root, text='1/x', padx=29, pady=15, command=operation.inverse)
        button_sqr = Button(self.root, text='x²', padx=33, pady=15, command=operation.sqr)
        button_sqrt = Button(self.root, text='√x', padx=32, pady=15, command=operation.sqrt)
        button_percent = Button(self.root, text='%', padx=33, pady=15, command=operation.percent)

        # Put buttons on the screen

        button_1.grid(row=5, column=0)
        button_2.grid(row=5, column=1)
        button_3.grid(row=5, column=2)
        button_4.grid(row=4, column=0)
        button_5.grid(row=4, column=1)
        button_6.grid(row=4, column=2)
        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)
        button_0.grid(row=6, column=1)

        button_add.grid(row=5, column=3)
        button_subtract.grid(row=4, column=3)
        button_multiply.grid(row=3, column=3)
        button_divide.grid(row=2, column=3)
        button_opposite.grid(row=6, column=0)
        button_comma.grid(row=6, column=2)
        button_equal.grid(row=6, column=3)

        button_percent.grid(row=1, column=0)
        button_clearentry.grid(row=1, column=1)
        button_clear.grid(row=1, column=2)
        button_backspace.grid(row=1, column=3)
        button_inverse.grid(row=2, column=0)
        button_sqr.grid(row=2, column=1)
        button_sqrt.grid(row=2, column=2)
