from tkinter import *

top = Tk()
groceryList = []

def results():
    results = E1.get()
    print(results)
    print(type(results))

def addToList():
    newItem = E1.get()
    groceryList.append(newItem)
    E1.delete(0, END)

def exportList():
    with open ('test.txt', 'w') as f:
        for item in groceryList:
            f.write("%s\n" % item)

#This is a Label widget
L1 = Label(top, text = "Grocery List")
L1.grid(column = 0, row = 1)

#This is a Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#This is a Button widget
B1 = Button(text = "    Print Your List    ", bg = "#d6fded", command = results)
B1.grid(column = 1, row = 2)
B2 = Button(text = "    Add to List    ", bg = "#ff00ed", command = addToList)
B2.grid(column = 0, row = 3)
B3 = Button(text = "    Export List    ", bg = "#e4a29f", command = exportList)
B3.grid(column = 1, row = 3)

top.mainloop()
