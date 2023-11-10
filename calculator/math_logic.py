from tkinter import END


class MathLogic:

    def __init__(self, entry_box):

        self.e = entry_box
        # Following self.e.get, self.e.insert, self.e.delete commands refer to Entry Box

        self.first_operation = "1"
        # self.first_operation is used to calculate properly with multiple analogical operations (2 * 2 * 2 ...)
        # "1" for first operation, "0" for not-fist analogical operations

        self.num1 = 0
        # self.num1 is first given number for mathematical operation

        self.num2 = 0
        # self.num2 is second given number for mathematical operation

        self.operation = ""
        # self.operation is used to determine mathematical operation (adding, subtracting, multiplying, dividing)

        self.result = 0
        # self.result is a result of mathematical operation

    ### Math ops ###

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
                self.e.insert(0, "Cannot divide by zero!")
                return
        elif self.operation == "":
            # Elif statement is used to return a number if no operation has been selected
            self.result = self.num2

        # "If" statement is used in order to correctly display integers (1.0 -> 1)
        if self.result - int(self.result) == 0:
            self.e.insert(0, int(self.result))
        else:
            self.e.insert(0, round(self.result, 10))

        # Set "self.first_operation" to "0" to allow multiple operations
        self.first_operation = "0"
        if self.first_operation == "0":
            self.num1 = self.result

    def button_add(self):
        self.operation = 'add'
        self.str2float()
        self.e.delete(0, END)
        self.first_operation = "1"

    def button_subtract(self):
        self.operation = 'subtract'
        self.str2float()
        self.e.delete(0, END)
        self.first_operation = "1"

    def button_multiply(self):
        self.operation = 'multiply'
        self.str2float()
        self.e.delete(0, END)
        self.first_operation = "1"

    def button_divide(self):
        self.operation = 'divide'
        self.str2float()
        self.e.delete(0, END)
        self.first_operation = "1"

    ### Others ops ###

    def click(self, digit):
        current = self.e.get()
        self.e.delete(0, END)

        if digit == "." in current:
            self.e.insert(0, current)
            # If statement used to not permit insertion more than 1 dot
        elif current == "0" and digit != ".":
            self.e.insert(0, digit)
            # If statement used to not permit insertion more than 1 zero, if the zero is first digit in entry
        elif " " in current and digit != ".":
            self.e.insert(0, digit)
            # If statement used to allow the insertion of a number after an Error Message 1/0 or sqrt(-1))
        elif " " in current and digit == ".":
            self.e.insert(0, current)
            # If statement used to not permit insertion a dot after an Error Message (1/0 or sqrt(-1))
        else:
            self.e.insert(0, current + digit)
            # All OK.

        self.first_operation = "1"

    def clear(self):
        self.e.delete(0, END)
        self.e.insert(0, "0")

        # Following variables set to default values otherwise after selecting
        # a number (1-9) and clicking "=", the entry box always returns 0
        self.num1 = 0
        self.num2 = 0
        self.result = 0
        self.operation = ""
        self.first_operation = "1"

    def clearentry(self):
        self.e.delete(0, END)
        self.e.insert(0, "0")

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
            outcome = int(1 / num)
            self.e.insert(0, outcome)
        else:
            self.e.insert(0, 1 / num)

    def sqr(self):
        self.str2float()
        self.e.delete(0, END)
        self.e.insert(0, self.num1 ** 2)

    def sqrt(self):
        try:
            num = float(self.e.get()) ** 0.5
            self.e.delete(0, END)
            if num - int(num) == 0:
                self.e.insert(0, int(num))
            else:
                self.e.insert(0, num)
        except TypeError or ValueError:
            self.e.insert(0, "Sqrt number cannot be lesser than 0!")

    def percent(self):
        if self.e.get() != "":
            num = float(self.e.get())
            num = num / 100
            self.e.delete(0, END)
            self.e.insert(0, num)
        else:
            num = self.num1 / 100
            self.e.insert(0, num)

    def str2float(self):
        try:
            self.num1 = float(self.e.get())
        except ValueError:
            pass
