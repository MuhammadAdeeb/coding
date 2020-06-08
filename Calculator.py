from tkinter import *
from tkinter import ttk


class Calculator:
    calc_value = 0.0
    num_check = False

    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):

        # To reset screen when new eqn is about to be entered
        if self.num_check:
            self.number_entry.delete(0, END)
            self.num_check = False  # Done so if user enters num>9, calculator doesn't clear screen

        entry_val = self.number_entry.get()  # get the number pressed
        entry_val += value  # add on the 2nd, 3rd or so on numbers pressed after the first one

        self.number_entry.delete(0, "end")  # delete the entry

        self.number_entry.insert(0, entry_val)  # Enter the full string of numbers entered so far

    def isfloat(self, str_val):
        # return true or false if string is a float
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        self.num_check = False  # Done so button_press knows to not clear the screen
                                # Do math with current number

        # print("\nNumber_Entry: " + self.number_entry.get())  # Debug
        # print("Entry_Value(Varchar): " + self.entry_value.get() + "\n")  # Debug
        if self.isfloat(str(self.number_entry.get())):
            self.calc_value = float(self.entry_value.get())

        # Triggers to know which math operation has to be done
        self.div_trigger = False
        self.mult_trigger = False
        self.add_trigger = False
        self.sub_trigger = False

        # print("---HERE---")  # debug

        if value == "/":
            print("/ Pressed ")  # for debugging
            self.div_trigger = True
        elif value == "*":
            print("* Pressed ")  # for debugging
            self.mult_trigger = True
        elif value == "+":
            print("+ Pressed ")  # for debugging
            self.add_trigger = True
        elif value == "-":
            print("- Pressed ")  # for debugging
            self.sub_trigger = True

        self.number_entry.delete(0, "end")

    def equal_button_press(self):
        if self.add_trigger or self.sub_trigger or self.div_trigger or self.mult_trigger:

            a = str(self.calc_value)
            b = str(self.number_entry.get())
            if self.add_trigger:
                c = "+"
            elif self.sub_trigger:
                c = "-"
            elif self.mult_trigger:
                c = "*"
            else:
                c = "/"

            # print("Calc_Value: " + str(self.calc_value))
            # print("Number_Entry: " + str(self.number_entry.get()))

            is_num_there_after_sign = True

            if not self.isfloat(self.number_entry.get()):
                is_num_there_after_sign = False
                solution = "MUST ENTER ANOTHER NUMBER BEFORE = "

            if is_num_there_after_sign:

                if self.add_trigger:
                    solution = self.calc_value + float(self.number_entry.get())
                    self.calc_value = 0.0

                elif self.sub_trigger:
                    solution = self.calc_value - float(self.entry_value.get())
                    self.calc_value = 0.0

                elif self.mult_trigger:
                    solution = self.calc_value * float(self.entry_value.get())
                    self.calc_value = 0.0

                elif self.div_trigger:
                    try:
                        solution = self.calc_value / float(self.entry_value.get())
                    except ZeroDivisionError:
                        # print("CAN'T DIVIDE W/ ZERO!!")
                        solution = "CAN'T DIVIDE W/ ZERO!"
                    self.calc_value = 0.0

            # self.history_text = a + " " + c + " " + b + " = " + str(solution) + "\n" + self.history_text

            print(a, " ", c, " ", b, " = ", solution)

            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False

            self.num_check = True
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)

    def clear_clicked(self):
        self.number_entry.delete(0, END)
        print("AC Pressed")

    def __init__(self, root):  # needs root object to work w/ our interface

        # The text in the Entry/Display of Calculator
        self.entry_value = StringVar(root, value="")

        root.title("Calculator")

        root.geometry("380x175")  # width by height

        root.resizable(width=False, height=False)
        # root.configure(bg="black")
        style = ttk.Style()

        style.configure("TButton",
                        font="Serif 10",
                        padding=5,
                        borderwidth=10)

        style.configure("TEntry",
                        font="Serif 50",
                        padding=10)

        '''
        self.history_text = ""
        self.history = Label(root, textvariable=self.history_text, justify="right")
        self.history.grid(row=5, column=0, columnspan=4, rowspan=5)
        '''
        # Entry: The display on top
        self.number_entry = ttk.Entry(root,
                                      textvariable=self.entry_value,
                                      width=59)

        self.number_entry.grid(row=0, columnspan=4)

        #  ---- 1st Row ----
        self.button7 = ttk.Button(root,
                                  text="7",
                                  command=lambda: self.button_press('7')).grid(row=1, column=0)

        self.button8 = ttk.Button(root,
                                  text="8",
                                  command=lambda: self.button_press('8')).grid(row=1, column=1)

        self.button9 = ttk.Button(root,
                                  text="9",
                                  command=lambda: self.button_press('9')).grid(row=1, column=2)

        self.button_div = ttk.Button(root,
                                     text="/",
                                     command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        # --- 2nd Row ---
        self.button4 = ttk.Button(root,
                                  text="4",
                                  command=lambda: self.button_press('4')).grid(row=2, column=0)

        self.button5 = ttk.Button(root,
                                  text="5",
                                  command=lambda: self.button_press('5')).grid(row=2, column=1)

        self.button6 = ttk.Button(root,
                                  text="6",
                                  command=lambda: self.button_press('6')).grid(row=2, column=2)

        self.button_mul = ttk.Button(root,
                                     text="*",
                                     command=lambda: self.math_button_press('*')).grid(row=2, column=3)

        # --- 3rd Row ---
        self.button1 = ttk.Button(root,
                                  text="1",
                                  command=lambda: self.button_press('1')).grid(row=3, column=0)

        self.button2 = ttk.Button(root,
                                  text="2",
                                  command=lambda: self.button_press('2')).grid(row=3, column=1)

        self.button3 = ttk.Button(root,
                                  text="3",
                                  command=lambda: self.button_press('3')).grid(row=3, column=2)

        self.button_add = ttk.Button(root,
                                     text="+",
                                     command=lambda: self.math_button_press('+')).grid(row=3, column=3)

        # --- 4rth Row ---
        self.button_clear = ttk.Button(root,
                                  text="AC",
                                  command=self.clear_clicked).grid(row=4, column=0)

        self.button0 = ttk.Button(root,
                                  text="0",
                                  command=lambda: self.button_press('0')).grid(row=4, column=1)

        self.button_equal = ttk.Button(root,
                                    text = "=",
                                    command=lambda: self.equal_button_press()).grid(row=4, column=2)

        self.button_sub = ttk.Button(root,
                                     text="-",
                                     command=lambda: self.math_button_press('-')).grid(row=4, column=3)


root = Tk()
calc = Calculator(root)

root.mainloop()


