from tkinter import *

root = Tk()
root.title("Simple Calculator")  # Window's Title

global num_tr  # Trigger/Bool for when a num is clicked
num_tr = False  # B/c when the program starts no num is clicked

global f_num  # Variable for storing the first number clicked for math eqn
global second_num  # Variable for storing the second number clicked for math eqn

global new_num  # Bool for start of a new math eqn
new_num = False  # New eqn doesn't start until at least one eqn is finished

# Tr/Bools for math operations
global add_tr
global sub_tr
global mul_tr
global div_tr

add_tr = False
sub_tr = False
mul_tr = False
div_tr = False

global empty_screen # Bool to know if there's no nums on the screen
empty_screen = True

# Create and place the entry:
e = Entry(root, width=52, borderwidth=5)
e.grid(row=0, column=0, ipady=8, columnspan=4)  # columnspan: span for 4 columns   b/c we'll have 4 cols underneath for num buttons


def num_clicked(num):
    global num_tr
    global new_num
    global empty_screen

    num_tr = True  # Number has been entered
    empty_screen = False  # Screen is not empty

    if new_num:  # New eqn is starting so delete the last answer
        print("IN NEW NUM, in num_clicked")
        e.delete(0, END)
        new_num = False

    num_entered = str(e.get())  # Gets the info from the screen
    num_entered += num  # To correctly store the whole sequence of nums being entered (for nums > 9 )

    e.delete(0, END)  # empty the screen
    e.insert(0, num_entered)  # Put the whole sequence of nums entered back on the screen


def equal_clicked():
    global add_tr
    global sub_tr
    global mul_tr
    global div_tr
    global num_tr  # Tr to know if/when a num is clicked
    global new_num   # Tr to know if a new math eqn is starting
    global f_num
    global second_num

    # To check if data in entry is a float
    isfloat = True
    try:
        float(e.get())
    except ValueError:
        isfloat = False

    if isfloat:  # Handles situations where if user doesn't click a num after a math operation and hits =

        # if/else: To do "Automatic Math"; Use the last math operator and operand and apply on the previous answer
        if not num_tr:
            f_num = float(e.get())  # f_num = last answer; b/c second_num is stored from last eqn & now we are just
            # gonna apply that and last operator to the answer we got on the screen

            e.delete(0, END)  # Clear screen to enter the answer from following lines of code
        else:
            second_num = float(e.get())  # second_num = num entered
            e.delete(0, END)  # Clear screen to enter the answer from following lines of code

        if add_tr:
            e.insert(0, f_num + second_num)
        elif sub_tr:
            e.insert(0, f_num - second_num)
        elif mul_tr:
            e.insert(0, f_num * second_num)
        elif div_tr:
            try:  # Handles Division by Zero
                e.insert(0, f_num / second_num)
            except ZeroDivisionError:
                e.insert(0, "Can't Divide With Zero!!")
        else:
            pass

    else:
        e.delete(0, END)  # Clear screen so nothing from b4 goes along w/ the text below
        e.insert(0, "You Must Enter A Number Before = sign!!")

    # Used to let num_clicked() know that a new eqn is starting; so it can clear the screen
    new_num = True
    num_tr = False  # set num_tr to False for "Automatic math"


def sign_clicked(sign):
    global add_tr
    global sub_tr
    global mul_tr
    global div_tr
    global f_num
    global new_num

    add_tr = False
    sub_tr = False
    mul_tr = False
    div_tr = False

    # To let user user know no math can be done w/o a num
    if empty_screen:
        new_num = True
        e.delete(0, END)
        e.insert(0, "You Must Enter A Number Before An Operator! ")
    else:
        if sign == '+':
            add_tr = True
        elif sign == '-':
            sub_tr = True
        elif sign == '*':
            mul_tr = True
        else:
            div_tr = True

        '''
        try:
            f_num = float(e.get())
        except ValueError:
            pass
        '''
        e.delete(0, END)


def clear_clicked():
    global empty_screen
    empty_screen = True  # T0 let rest of the functions know screen is empty and behave accordingly
    e.delete(0, END)


# ---Row 1---
# Creating Buttons:
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: num_clicked('7'))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: num_clicked('8'))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: num_clicked('9'))
# Placing on the grid:
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

# ---Row 2---
# Creating Buttons:
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: num_clicked('4'))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: num_clicked('5'))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: num_clicked('6'))
# Placing on the grid:
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

# ---Row 3---
# Creating Buttons:
b1 = Button(root, text="1", padx=40, pady=20, command=lambda: num_clicked('1'))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: num_clicked('2'))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: num_clicked('3'))
# Placing on the grid:
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

# ---Row 4---
# Creating Buttons:
b0 = Button(root, text="0", padx=40, pady=20, command=lambda: num_clicked('0'))
b_add = Button(root, text="+", padx=38, pady=20, command=lambda: sign_clicked('+'))
b_equal = Button(root, text="=", padx=87, pady=20, command=equal_clicked)
# Placing on the grid:
b0.grid(row=4, column=0)
b_add.grid(row=4, column=3)
b_equal.grid(row=4, column=1, columnspan=2)


# ---Row 5---
b_clear = Button(root, text="CLEAR", padx=169, pady=5, justify="center", command=clear_clicked)  # Creating Button
b_clear.grid(row=5, column=0, columnspan=4)  # Placing on the grid


# ---Rest of the math signs---
# Creating Buttons:
b_sub = Button(root, text="-", padx=39, pady=20, command=lambda: sign_clicked('-'))
b_mul = Button(root, text="*", padx=39, pady=20, command=lambda: sign_clicked('*'))
b_div = Button(root, text="/", padx=39, pady=20, command=lambda: sign_clicked('/'))
# Placing on the grid:
b_sub.grid(row=1, column=3)
b_mul.grid(row=2, column=3)
b_div.grid(row=3, column=3)

root.mainloop()  # To continuously run the window
