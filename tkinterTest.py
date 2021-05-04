from tkinter import *

top = Tk()
groceryList = []

def results():
    print(groceryList)

def addToList():
    newItem = E1.get()
    groceryList.append(newItem)

#This is a Label widget
L1 = Label(top, text = "Grocery List")
L1.grid(column = 0, row = 1)

#This is a Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#This is a Button widget
B1 = Button(text = "    Print List    ", bg = "green", command = results)
B1.grid(column = 0, row = 3)

B2 = Button(text = "    Add to List    ", bg = "green", comand = addToList)
B2.grid(column = 1, row = 2)

top.mainloop()
