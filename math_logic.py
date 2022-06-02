from tkinter import *


class Calculator:

    def __init__(self, entry_box):

        self.e = entry_box
        # Following self.e.get, self.e.insert, self,e.delete commands refer to Entry Box

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

### Math methods ###

    def equal(self):

        # "If" statement is used to allow quick multiple calculation. Example input: "2 * = ="  => "2 * 2 * 2 ="
        if self.first_operation == "1":
            try:
                self.num2 = float(self.e.get())
            except ValueError:
                self.num2 = self.num1
        self.e.delete(0, END)


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
                self.e.insert(0, "Nie można dzielić przez zero")
        elif self.operation == "":
            self.result = self.num2


        # "If" statement is used in order to correctly display integers (1.0 -> 1)
        if self.result - int(self.result) == 0:
            self.e.insert(0, int(self.result))
        else:
            self.e.insert(0, round(self.result, 10))


        # Set "self.first_operation" to "0" to allow multiple operations

        if self.first_operation == "0":
            self.num1 = self.result
        self.first_operation = "0"

    def button_add(self):
        self.operation = 'add'
        if str2int(self.e.get()):
            self.num1 = int(self.e.get())
        else:
            self.num1 = float(self.e.get())
        self.e.delete(0, END)
        self.first_operation = "1"

    def button_subtract(self):
        self.operation = 'subtract'
        if str2int(self.e.get()):
            self.num1 = int(self.e.get())
        else:
            self.num1 = float(self.e.get())
        self.e.delete(0, END)
        self.first_operation = "1"

    def button_multiply(self):
        self.operation = 'multiply'
        if str2int(self.e.get()):
            self.num1 = int(self.e.get())
        else:
            self.num1 = float(self.e.get())
        self.e.delete(0, END)
        self.first_operation = "1"

    def button_divide(self):
        self.operation = 'divide'
        self.num1 = float(self.e.get())
        self.e.delete(0, END)
        self.first_operation = "1"


    ### Others methods ###

    def click(self, digit):
        current = self.e.get()
        self.e.delete(0, END)

        # set 0 as the default number
        if digit == "." in current:
            pass
            self.e.insert(0, current)
        elif current == "0" and digit != ".":
            self.e.insert(0, digit)
        else:
            self.e.insert(0, current + digit)

    def clear(self):
        self.e.delete(0, END)
        self.e.insert(0, "0")

        #fix error: after selecting a number and clicking "=", the entry box always returns 0
        self.num1 = 0
        self.num2 = 0
        self.result = 0
        self.first_operation = "1"

    # Do uzupelnienia
    def clearentry(self):
        return

    def opposite(self):
        num = self.e.get()
        self.e.delete(0, END)
        num = float(num)
        if num.is_integer():
            self.e.insert(0, int(-num))
        else:
            self.e.insert(0, -num)

    def backspace(self):
        self.e.delete(self.e.index("end") - 1)
        # If statement used in case if all digits were backspaced
        if self.e.get() == "":
            self.e.insert(0, "0")


    def inverse(self):
        num = float(self.e.get())
        self.e.delete(0, END)
        if (1 / num).is_integer():
            wynik = int(1 / num)
            self.e.insert(0, wynik)
        else:
            self.e.insert(0, 1 / num)

    def sqr(self):
        if str2int(self.e.get()):
            num = int(self.e.get())
        else:
            num = float(self.e.get())
        self.e.delete(0, END)
        self.e.insert(0, num ** 2)

    def sqrt(self):
        num = float(self.e.get()) ** 0.5
        self.e.delete(0, END)
        try:
            if num - int(num) == 0:
                self.e.insert(0, int(num))
            else:
                self.e.insert(0, num)
        except ZeroDivisionError:
            self.e.insert(0, int(num))

    def percent(self):
            if self.e.get() != "":
                num = float(self.e.get())
                num = num / 100
                self.e.delete(0, END)
                self.e.insert(0, num)
            else:
                num = self.num1 / 100
                self.e.insert(0, num)


def str2int(string_number):
    try:
        int(string_number)
        return True
    except (TypeError, ValueError):
        return False


