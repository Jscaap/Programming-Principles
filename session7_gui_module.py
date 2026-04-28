'''
# example 1
# Plain GUI Window
# (1) import tkinter library
from tkinter import *
# (2) Instantiating top level
window = Tk()
# (3) Setting the title of the window
window.title('Hello Students of ICT105')
# (4) Setting the geometry i.e Dimensions
window.geometry("300x200+10+20")
# (5) Mainloop which will cause this toplevel to run infinitely
window.mainloop()
'''

# example 2
from tkinter import *
window = Tk()
# Add an input field with the label "Name"
name_label = Label(window, text="Name:")
name_label.grid(row=0, column=0)
name_entry = Entry(window)
name_entry.grid(row=0, column=1)
# Function to print the entered name to stdout
def print_name():
    name = name_entry.get()
    print("Name:", name)
# Add a button to trigger the print function
print_button = Button(window, text="Print Name", command=print_name)
print_button.grid(row=1, columnspan=2)
window.title('Hello Students of ICT105')
window.geometry("300x200+10+20")
window.mainloop()