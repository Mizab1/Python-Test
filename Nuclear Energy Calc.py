import tkinter as tk
from tkinter import Canvas, ttk
from tkinter.ttk import *
from ttkthemes import themed_tk as tk
import time
import os
import sys
import math

root = tk.ThemedTk()
root.get_themes()
root.set_theme("breeze")
root.geometry('400x200')
root.title("Uranium Needed Calculator")

result = 0
def click_submit():
    result_get = main_text_box.get()

    result_get = int(result_get)
    solved_result_uranium = result_get
    solved_result_coal = result_get * 3
    solved_result_oil = result_get * 600
    converted_result_coal = str(solved_result_coal)
    converted_result_uranium = str(solved_result_uranium)
    converted_result_oil = str(solved_result_oil)

    result_var_uranium = "Required Uranium is:" + converted_result_uranium + " gm"
    result_var_oil = "Required Oil is:" + converted_result_oil + " gallon(s)"
    result_var_coal = "Required Coal is:" + converted_result_coal + " ton(s)"

    result_print = ttk.Label(root, font= "helvetica 12 bold")
    result_print.config(text=result_var_uranium)
    result_print.grid(sticky='nw', row=3, column=0, pady=5, padx=5, columnspan=2)

    result_print = ttk.Label(root, font= "helvetica 12 bold")
    result_print.config(text=result_var_oil)
    result_print.grid(sticky='nw', row=4, column=0, pady=5, padx=5, columnspan=2)

    result_print = ttk.Label(root, font= "helvetica 12 bold")
    result_print.config(text=result_var_coal)
    result_print.grid(sticky='nw', row=5, column=0, pady=5, padx=5, columnspan=2)


text_box_text = ttk.Label(root, text="Enter the amount of electricity needded (in MW)").grid(sticky='nw', row=0, column=0, pady=5)
main_text_box = ttk.Entry(root, width=30, textvariable= result)
main_text_box.grid(sticky='nw', row=0, column=1)

submit_button = ttk.Button(text="Submit", width=30, command=click_submit).grid(sticky='nw', row=2, column=0, columnspan=2, padx=70, pady= 10)


root.mainloop()

