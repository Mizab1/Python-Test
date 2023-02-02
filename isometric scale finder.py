import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from ttkthemes import themed_tk as tk
import time
import os
import sys
import math

root = tk.ThemedTk()
root.get_themes()
root.set_theme("breeze")
root.geometry('300x150')
root.title("ISC")

result = 0
def click_submit():
    result_get = main_text_box.get()
    result_get = int(result_get)
    solved_result = result_get * 0.82
    converted_result = str(solved_result)
    result_var = "Your Result is:" + converted_result + " cm"
    result_print = ttk.Label(root, font= "helvetica 12 bold")
    result_print.config(text=result_var)
    result_print.grid(sticky='nw', row=3, column=0, pady=5, padx=5, columnspan=2)


text_box_text = ttk.Label(root, text="Enter the Text here(in: cm):").grid(sticky='nw', row=0, column=0, pady=5)
main_text_box = ttk.Entry(root, width=30, textvariable= result)
main_text_box.grid(sticky='nw', row=0, column=1)

submit_button = ttk.Button(text="Submit", width=30, command=click_submit).grid(sticky='nw', row=2, column=0, columnspan=2, padx=30, pady= 10)


root.mainloop()

