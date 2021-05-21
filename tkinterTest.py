from tkinter import *
import random
import datetime
import tkinter as tk

top = Tk()
groceryList = []
myRolls = []
rollTimes = 0
dieType = 0

def exportList():
    with open ('test.txt', 'w') as f:
        for item in groceryList:
            f.write("%s\n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 3, row = 1)
    
    B1Main = Button(text = "    Week 1    ", bg = "#9966ff", command = week1)
    B1Main.grid(column = 3, row = 2)
    
    B2Main = Button(text = "    Week 2    ", bg = "#ffcc66", command = week2)
    B2Main.grid(column = 3, row = 3)
    
    B3Main = Button(text = "    Week 3     ", bg = "#009999", command = week3)
    B3Main.grid(column = 3, row = 4)

def week1():
    
    def results():
        results = E1.get()
        print(results)
        print(type(results))
    
    def addToList():
        newItem = E1.get()
        groceryList.append(newItem)
        E1.delete(0, END)
    
    clearWindow()
    #This is a Label widget
    L1 = Label(top, text = "Grocery List")
    L1.grid(column = 0, row = 1)


    #This is a Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a Button widget
    B1 = Button(text = "    Print Your List    ", bg = "#d6fded", command = results)
    B1.grid(column = 0, row = 3)
    
    B2 = Button(text = "    Add to List    ", bg = "#ff00ed", command = addToList)
    B2.grid(column = 1, row = 2)
    
    B3 = Button(text = "    Export List    ", bg = "#e4a29f", command = exportList)
    B3.grid(column = 0, row = 4)

    
    Bclear = Button(text = "    Clear Window    ", bg = "#ffff99", command = mainMenu)
    Bclear.grid(column = 1, row = 3)

def week2():
    def rollDice():
        #upate our variable data
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        
        #clear window AFTER pulling Entry data
        clearWindow()
        
        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
            
        #display dice rolls and present and exit button
        L4W2 = Label(top, text = "Here are your rolls!")
        L4W2.grid(column = 0, row = 1)
        #this one will use a .format() statement
        L5W2 = Label(top, text = "{}" .format(myRolls))
        L5W2.grid(column = 0, row = 2)
        
        B2W2 = Button(text = "Main Menu", bg = "#ffccff", command = mainMenu)
        B2W2.grid(column = 0, row = 3)

def week3():
    def ageGenerator():
        window=tk.Tk()
        window.geometry("620x780")
        window.title(" Age Calculator App ")

        #This is a Label widget
        name = tk.Label(text = "Name")
        name.grid(column = 0, row = 1)
        year = tk.Label (text = "Year")
        year.grid(column = 0, row = 2)
        month = tk.Label(text = "Month")
        month.grid(column = 0, row = 3)
        dtae = tk.Label(text = "Day")
        date.grid(column = 0, row = 4)

        #This is a Entry widget
        nameEntry = tk.Entry()
        nameEntry.grid(column = 1, row =1)
        yearEntry = tk.Entry()
        yerEntry.grid(column = 1, row = 2)
        monthEntry = tk.Entry()
        monthEntry.grid(column = 1, row = 3)
        dateEntry = tk.Entry
        dateEntry.grid(column = 1, row = 4)
        
    def getInput():
        name=nameEntry.get()
        monkey = Person(name,datetime.date(int(yearEntry.get()), int(montEntry.get()), int(dateEntry.get())))
        textArea = tl.Text(master=window,height=10,width=25)
        textArea.grid(column = 1, row = 6)
        answer = " Heyy (monkey)!!!. You are (age) years old!!! ".format(monkey=name, age=monkey.age())
        textArea.insert(tk.END, answer)
    button=tk.Button(window, text = "Calculate Age", command = get, bg = "pink")
    
    clearWindow()
    L1W2 = Label(text="Dice Roller Program")
    L1W2.grid(column = 0, row = 1)
    
    L2W2 = Label(top, text = "How many sides?")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text = "How many  rolls?")
    L3W2.grid(column = 2, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)

    B1W2 = Button(text="Roll", bg= "#ccff99", command = rollDice)
    B1W2.grid(column = 2, row = 4)

    #to add: roll function and exit button
    

if __name__ == "__main__":
    mainMenu()
    top.mainloop()
