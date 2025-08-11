from tkinter import *

window = Tk()

window.title("Welcome to app")

window.geometry('500x450')

lbl = Label(window, text="")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me")
btn = Button(window, text="Click Me", bg="orange", fg="red")
btn.grid(column=20, row=20)

window.mainloop()
