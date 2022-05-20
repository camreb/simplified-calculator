from tkinter import *

root = Tk()
root.geometry('350x370')
root.title("Calculator")


# Define Entry Box
# Following e.get, e.insert, e.delete commands refer to Entry Box
e = Entry(root, width=40)
# Put Entry Box on the screen
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

class Calculator:

    def __init__(self):
        self.first_operation = "1"
        # self.first_operation is used to calculate properly with multiple analogical operations (2 * 2 * 2 ...)
        # "1" for first operation, "0" for not-fist analogical operations

        self.num1 = 0
        # self.num1 is first given number for mathematical operation

        self.num2 = 0
        # self.num2 is second given number for mathematical operation

        self.operation = ""
        #self.operation is used to determine mathematical opeartion (adding, subtracting, multiplying, dividing)

        self.result = 0
        # self.result is a result of mathematical operation


### Math method ###

    def button_equal(self):

        # "If" statement is used to allow quick multiple calculation. Example input: "2 * = ="  => "2 * 2 * 2 ="
        if self.first_operation == "1":
            try:
                self.num2 = float(e.get())
            except ValueError:
                self.num2 = self.num1
        e.delete(0, END)


        if self.operation == 'add':
            self.result = self.num1 + self.num2
        elif self.operation == 'subtract':
            self.result = self.num1 - self.num2
        elif self.operation == 'multiply':
            self.result = self.num1 * self.num2
        elif self.operation == 'divide':
            try:
                self.result = self.num1 / self.num2
            except ZeroDivisionError:
                e.insert(0, "Nie można dzielić przez zero")


        # "If" statement is used in order to correctly display integers (1.0 -> 1)
        if self.result - int(self.result) == 0:
            e.insert(0, int(self.result))
        else:
            e.insert(0, round(self.result, 10))


        # Set "self.first_operation" to "0" to allow multiple operations
        self.first_operation = "0"
        if self.first_operation == "0":
            self.num1 = self.result

    def button_add(self):
        self.operation = 'add'
        if str2int(e.get()):
            self.num1 = int(e.get())
        else:
            self.num1 = float(e.get())
        e.delete(0, END)
        self.first_operation = "1"

    def button_subtract(self):
        self.operation = 'subtract'
        if str2int(e.get()):
            self.num1 = int(e.get())
        else:
            self.num1 = float(e.get())
        e.delete(0, END)
        self.first_operation = "1"

    def button_multiply(self):
        self.operation = 'multiply'
        if str2int(e.get()):
            self.num1 = int(e.get())
        else:
            self.num1 = float(e.get())
        e.delete(0, END)
        self.first_operation = "1"

    def button_divide(self):
        self.operation = 'divide'
        self.num1 = float(e.get())
        e.delete(0, END)
        self.first_operation = "1"


### Others functions ###

def button_click(digit):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + digit)

def button_clear():
    e.delete(0, END)

# Do uzupelnienia
def button_clearentry(self):
    return

def button_opposite():
    num = e.get()
    e.delete(0, END)
    num = float(num)
    if num.is_integer():
        e.insert(0, int(-num))
    else:
        e.insert(0, -num)

def button_backspace():
    e.delete(e.index("end") - 1)


def button_inverse():
    num = float(e.get())
    e.delete(0, END)
    if (1 / num).is_integer():
        wynik = int(1 / num)
        e.insert(0, wynik)
    else:
        e.insert(0, 1 / num)

def button_sqr():
    if str2int(e.get()):
        num = int(e.get())
    else:
        num = float(e.get())
    e.delete(0, END)
    e.insert(0, num ** 2)

def button_sqrt():
    num = float(e.get()) ** 0.5
    e.delete(0, END)
    try:
        if num - int(num) == 0:
            e.insert(0, int(num))
        else:
            e.insert(0, num)
    except ZeroDivisionError:
        e.insert(0, int(num))

def button_percent():
        if e.get() != "":
            num = float(e.get())
            num = num / 100
            e.delete(0, END)
            e.insert(0, num)
        else:
            num = self.num1 / 100
            e.insert(0, num)


def str2int(string_number):
    try:
        int(string_number)
        return True
    except (TypeError, ValueError):
        return False


calc = Calculator()


# Define buttons

button_1 = Button(root, text='1', padx=35, pady=15, command=lambda: button_click("1"))
button_2 = Button(root, text='2', padx=35, pady=15, command=lambda: button_click("2"))
button_3 = Button(root, text='3', padx=35, pady=15, command=lambda: button_click("3"))
button_4 = Button(root, text='4', padx=35, pady=15, command=lambda: button_click("4"))
button_5 = Button(root, text='5', padx=35, pady=15, command=lambda: button_click("5"))
button_6 = Button(root, text='6', padx=35, pady=15, command=lambda: button_click("6"))
button_7 = Button(root, text='7', padx=35, pady=15, command=lambda: button_click("7"))
button_8 = Button(root, text='8', padx=35, pady=15, command=lambda: button_click("8"))
button_9 = Button(root, text='9', padx=35, pady=15, command=lambda: button_click("9"))
button_0 = Button(root, text='0', padx=35, pady=15, command=lambda: button_click("0"))

button_add = Button(root, text='+', padx=34, pady=15, command=calc.button_add)
button_subtract = Button(root, text='-', padx=36, pady=15, command=calc.button_subtract)
button_multiply = Button(root, text='*', padx=36, pady=15, command=calc.button_multiply)
button_divide = Button(root, text='/', padx=36, pady=15, command=calc.button_divide)
button_opposite = Button(root, text='+/-', padx=29, pady=15, command=button_opposite)
button_equal = Button(root, text='=', padx=34, pady=15, command=calc.button_equal)
button_clear = Button(root, text='C', padx=35, pady=15, command=button_clear)
button_clearentry = Button(root, text='CE', padx=32, pady=15, command=button_clearentry)
button_comma = Button(root, text='.', padx=37, pady=15, command=lambda: button_click("."))

button_backspace = Button(root, text='<--', padx=29, pady=15, command=button_backspace)
button_inverse = Button(root, text='1/x', padx=29, pady=15, command=button_inverse)
button_sqr = Button(root, text='x²', padx=33, pady=15, command=button_sqr)
button_sqrt = Button(root, text='√x', padx=32, pady=15, command=button_sqrt)
button_percent = Button(root, text='%', padx=33, pady=15, command=button_percent)

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

root.mainloop()