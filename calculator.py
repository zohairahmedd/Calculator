from tkinter import *

root = Tk() # creates main window of an application
root.title("Calculator") # sets title of main window
root.configure(bg="#808080") # sets background colour for main window

e = Entry(root, width=21, borderwidth=2, bg="#808080", fg="white", font=("Helvetica", 22, "bold")) # defines characteristics of widget e - characteristics inside the window
e.grid(row=0, column=0, columnspan=4, padx=4, pady=5, ipadx=8, ipady=13) # places widget inside the main window with padding

def button_click(number): # function button_click with argument number
    current = e.get() # takes current text in entry widget
    e.delete(0, END) # deletes current text in entry widget from start to end
    e.insert(0, str(current) + str(number)) # inserts new text into the entry widget

def button_clear(): # function button_clear with no argument
    e.delete(0, END) # deletes all content fron entry widget

def button_add(): # function button_add with no argument
    first_number = e.get() # retrieves current value from entry widget - stores in first_number
    global f_num # global variable
    global math # global variables
    math = "addition" # math variable is assigned to the string addition
    f_num = float(first_number) # assigns integer value of first_number to f_num (global variable)
    e.delete(0, END) # deletes all content fron entry widget

def button_subtract(): # function button_subtract with no argument
    first_number = e.get() # retrieves current value from entry widget - stores in first_number
    global f_num # global variable  
    global math # global variable
    math = "subtraction" # math variable is assigned to the string subtraction
    f_num = float(first_number) # assigns integer value of first_number to f_num (global variable)
    e.delete(0, END) # deletes all content fron entry widget

def button_multiply(): # function button_multiply with no argument
    first_number = e.get() # retrieves current value from entry widget - stores in first_number
    global f_num # global variable  
    global math # global variable  
    math = "multiplication" # math variable is assigned to the string multiplication
    f_num = float(first_number) # assigns integer value of first_number to f_num (global variable)
    e.delete(0, END) # deletes all content fron entry widget

def button_divide(): # function button_multiply with no argument
    first_number = e.get() # retrieves current value from entry widget - stores in first_number
    global f_num # global variable  
    global math # global variable  
    math = "division" # math variable is assigned to the string multiplication
    f_num = float(first_number) # assigns integer value of first_number to f_num (global variable)
    e.delete(0, END) # deletes all content fron entry widget

def button_equal(): # function button_equal with no argument
    second_number = e.get() # retrieves current value from entry widget - stores in second_number
    e.delete(0, END) # deletes all content fron entry widget

    if math == "addition":
        e.insert(0, f_num + float(second_number)) # adds first and second number if math is addition
    if math == "subtraction":
        e.insert(0, f_num - float(second_number)) # subtracts first and second number if math is subtraction
    if math == "multiplication":
        e.insert(0, f_num * float(second_number)) # multiplies first and second number if math is multiplication
    if math == "division":
        e.insert(0, f_num / float(second_number)) # divides first and second number if math is division

# changing the look of each individual button on the calculator (colour, padding, lambda: takes any number of arguments, but can only have one expression)
button_1 = Button(root, text='1',bg="#4a503d",fg="white", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2',bg="#4a503d",fg="white", padx=41, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3',bg="#4a503d",fg="white", padx=39, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4',bg="#4a503d",fg="white", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5',bg="#4a503d",fg="white", padx=41, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6',bg="#4a503d",fg="white", padx=39, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7',bg="#4a503d",fg="white", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8',bg="#4a503d",fg="white", padx=41, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9',bg="#4a503d",fg="white", padx=39, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0',bg="#4a503d",fg="white", padx=87, pady=20, command=lambda: button_click(0))
button_dot = Button(root, text='.',bg="#4a503d",fg="white", padx=42.5, pady=20, command=lambda: button_click('.'))
button_add = Button(root, text='+',bg="#4a503d",fg="white", padx=39, pady=20, command= button_add)
button_equal = Button(root, text='=',bg="#4a503d",fg="white", padx=87, pady=20, command= button_equal)
button_clear = Button(root, text='AC',bg="#4a503d",fg="white", padx=34, pady=20, command= button_clear)
button_subtract = Button(root, text='-',bg="#4a503d",fg="white", padx=41, pady=20, command= button_subtract)
button_multiply = Button(root, text='*',bg="#4a503d",fg="white", padx=42, pady=20, command= button_multiply)
button_divide = Button(root, text='/',bg="#4a503d",fg="white", padx=40, pady=20, command= button_divide)

# positions number buttons at a specific location in the grid defined by row and column parameters | notice how nothing is in the same row & column
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0, columnspan=3)
button_dot.grid(row=4, column=2)

# positions operation buttons at a specific location in the grid defined by row and column parameters | notice how nothing is in the same row & column
button_clear.grid(row=5, column=3)
button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)

root.mainloop() # starts event loop from root = Tk() and onwards | listens for mouse clicks or keyboard input to update GUI or main window accordingly until window is closed