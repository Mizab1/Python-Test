

import pyautogui 
import webbrowser as wb
import time
import random

# wb.open("web.whatsapp.com")

time.sleep(5)

text = open("ascii", 'r')   
for word in text:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    #time.sleep(2)

# for i in range(5):
#     time_remaining = (i - 5) * -1
#     pyautogui.typewrite("Remaining time is: " + str(time_remaining) + " mins")
#     pyautogui.press("enter")
#     time.sleep(60)
    
#     pyautogui.press("enter")

# number_file = open("random_number", "w")
# for i in range(5000):
#     randomVal = random.randint(9000000000, 9999999999)
#     #randomlist.append(randomVal)
#     number_file.write(str(randomVal) + "\n")

# for i in range(1000):
#     # pyautogui.typewrite("‎")
#     pyautogui.hotkey('ctrl', 'v')
#     pyautogui.press("enter")

