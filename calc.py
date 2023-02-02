import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import time
import os
import sys
import math

# global x
# x = 0
# root = tk.Tk()


# root.title('Calculator')
# root.geometry('600x800')
# #root.configure(background="black")

# function_lable = tk.Label(root,text="List of Available Functions:").grid(row=0, column=0, sticky='w')

# function_selector = ttk.Combobox(root, width=25, textvariable = x, state = 'readonly')
# function_selector['values'] = (
#     'Area of Square',
#     'Volume of Sqaure',
#     'Area of Sphere',
#     'Volume of Sphere'
#     )
# function_selector.grid(row=0, column=1, sticky='w')

# submitfunction = tk.Button(width= 20, text="Confirm", textvariable=x).grid(row=2, column=0, sticky='w', padx=30, pady=20)
# print(x)
#lable = tk.Label(width= 20, text="Your selected funtion is" + submitfunction.get()).grid(row=2, column=0, sticky='w', padx=30, pady=20)

# blank_1 = tk.Label(text="").grid(row=1, column=0, sticky='w')

# first_entry_box_text = tk.Label(text="Write the first number").grid(row=2, column=0, sticky='w')
# first_entry_box = tk.Entry(width=15).grid(row=2, column=1, sticky='w')
# first_entry_box_text = tk.Label(text="Write the second number").grid(row=3, column=0, sticky='w')
# first_entry_box = tk.Entry(width=15).grid(row=3, column=1, sticky='w')

# submit = tk.Button(width= 20, text="Calculate").grid(row=4, column=0, sticky='w', padx=30, pady=20)



# root.mainloop()




# variables
def script():
    # functions
    def re_run(): # Re run
        run = str(input("\nDo you want to calculate more value (Y/N): "))
        while True:
            if run == "yes" or run == "y" or run == "Y":
                os.system('cls' if os.name == 'nt' else 'clear')
                script()
                break
            elif run == "no" or run == "n" or run == "N":
                print("Thanks for using!")
                time.sleep(2)
                sys.exit()
            else:
                print("Please write y or n OR yes or no")
                re_run()



    def input_variable_a():
        a = input("Enter you length: ")
        while True:
            try:
                n = float(a)
                a = float(a)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
                a = input("Enter you length: ")
        
        return a

    def input_variable_b():
        b = input("Enter you Width: ")
        while True:
            try:
                n = float(b)
                b = float(b)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
                b = int(input("Enter you Width: "))
        
        return b

    def input_variable_c():
        c = input("Enter you height: ")
        while True:
            try:
                n = float(c)
                c = float(c)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
                c = int(input("Enter you height: "))

        return c

    def input_variable_d():
        d = input("Enter the angle: ")
        while True:
            try:
                n = float(d)
                d = float(d)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
                d = input("Enter the angle: ")

        return d

    def input_variable_e():
        e = input("Enter the Radius: ")
        while True:
            try:
                n = float(e)
                e = float(e)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
                e = input("Enter the Radius: ")

        return e

    def input_variable_f():
        f = input("Enter the First Length: ")
        while True:
            try:
                n = float(f)
                f = float(f)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
                f = input("Enter the First Length: ")

        return f

    def input_variable_g():
        g = input("Enter the Second Length: ")
        while True:
            try:
                n = float(g)
                g = float(g)
                break
            except ValueError:
                print("No valid integer! Please try again ...")
                g = input("Enter the First Length: ")

        return g
        

    # Operation
    print("Following Formulas are available:")
    print("  Press their corresponding number to select them")
    print("    1 = Area")
    print("    2 = Volume")
    print("    3 = 2D Perimeter")
    print("    4 = Sin")
    print("    5 = Cos")
    print("    6 = Tan")
    print("    7 = Surface Area of Cube/Cuboid")
    print("    8 = Area of Triangle")
    print("    9 = Volume of Sphere")
    print("    10 = Area of Sphere")
    print("    11 = Area of Trapezium")
    x = input("Enter you formula you want to use: ")

    while True:
        try:
            x = int(x)
            while True:
                if x in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}:
                    break
                else:
                    print("Oops! I can't find the right operator")
                    x =input("Enter you formula you want to use: ")
            break
        except ValueError:
            print("No valid integer! Please try again ...")
            x =input("Enter you formula you want to use: ")

    # Check the operation and use the formula
    if x == 1:
        first_number = input_variable_a()
        second_number = input_variable_b()

        print("\nYour answer is: ")
        print(first_number * second_number)
        
    elif x == 2:
        first_number = input_variable_a()
        second_number = input_variable_b()
        third_number = input_variable_c()

        print("\nYour answer is: ")
        print(first_number * second_number * third_number)
        
    elif x == 3:
        first_number = input_variable_a()
        second_number = input_variable_b()

        local_2d_perimeter_1 = (first_number + second_number) * 2

        print("\nYour answer is: ")
        print(local_2d_perimeter_1)
        
    elif x == 4:
        forth_number = input_variable_d()

        local_sin = math.sin(forth_number)

        print("\nYour answer is: ")
        print(local_sin)
        

    elif x == 5:
        forth_number = input_variable_d()

        local_sin = math.cos(forth_number)

        print("\nYour answer is: ")
        print(local_sin)
        

    elif x == 6:
        forth_number = input_variable_d()

        local_sin = math.tan(forth_number)

        print("\nYour answer is: ")
        print(local_sin)

    elif x == 7:
        first_number = input_variable_a()
        second_number = input_variable_b()
        third_number = input_variable_c()

        local_sa =  (first_number + second_number) * third_number

        print("\nYour answer is: ")
        print(local_sa)

    elif x == 8:
        second_number = input_variable_b()
        third_number = input_variable_c()

        local_sa =  (second_number + third_number) / 2

        print("\nYour answer is: ")
        print(local_sa)

    elif x == 9:
        first_number = input_variable_e()

        local_sa =  4 / 3 * math.pi * first_number**3

        print("\nYour answer is: ")
        print(local_sa)

    elif x == 10:
        first_number = input_variable_e()

        local_sa =  4 * math.pi * first_number**2

        print("\nYour answer is: ")
        print(local_sa)

    elif x == 11:
        first_number = input_variable_f()
        second_number = input_variable_g()
        third_number = input_variable_c()

        local_sa =  (first_number + second_number) / 2 * third_number

        print("\nYour answer is: ")
        print(local_sa)




    re_run()


# Run
script()