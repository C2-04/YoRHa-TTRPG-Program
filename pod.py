#oh boy, a GUI
from CommanderWhite import *
from InstructorBlack import *
from masamune import *
from Anemone import *
from TwoB import *
from tkinter import *
import tkinter.ttk as ttk
root = Tk()
root.geometry("1000x1000")
root.configure(background="#c8c6ae")
frame = Frame(root)
frame.pack()
def makeUnitList():
    def retrieve():
        selected = listbox.curselection()[0]
        result = listbox.get(selected, selected)
        print(result[0])
        printStats(result[0])
        return result(0)
    listbox = Listbox(root)  
    with open('savedata/YoRHa Registry', 'rb') as infile:
        units = pickle.load(infile)
        infile.close()
    i=1
    for element in units:
        if element != '' :
            listbox.insert(i,element)  
            i = i+1
    bttn = Button(frame, text = "Submit", command = retrieve)
    bttn.pack(side= "bottom")
    listbox.pack()
leftframe = Frame(root)
leftframe.pack(side=LEFT)
leftframe.configure(background="#c8c6ae")
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
rightframe.configure(background="#c8c6ae")
def enpassant():
    print('google en passant')
label = Label(frame, text = "Welcome, Commander.",font = ("FOT-Rodin Pro DB", 30), bg="#c8c6ae")
label.pack()
mainmenu = Menu(frame)
root.config(menu = mainmenu)
# Menu 1
adminmenu = Menu(mainmenu, tearoff = 0)
adminmenu.add_command(label = "Open", command = enpassant)
adminmenu.add_command(label = "List Units", command = listunits)
adminmenu.add_command(label = "Print The Cube", command = printTable)
adminmenu.add_command(label = "View Unit", command = makeUnitList)
adminmenu.add_separator()
adminmenu.add_command(label = "Exit", command = root.destroy)
mainmenu.add_cascade(label="Administrative", menu=adminmenu)

# Menu 2
missionmenu = Menu(mainmenu, tearoff = 0)
missionmenu.add_command(label = "Find", command = enpassant)
missionmenu.add_command(label = "Debugger", command = enpassant)
missionmenu.add_command(label = "Replace", command = enpassant)
mainmenu.add_cascade(label="Missions", menu=missionmenu)

root.title("YoRHa TTRPG Program")
root.mainloop()
