from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to Pranit E-Learnings app")

window.geometry('350x200')

chk_state = BooleanVar()

chk_state.set(True) #set check state

chk = Checkbutton(window, text='Select', var=chk_state)

chk.grid(column=0, row=0)

window.mainloop()
