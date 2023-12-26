### import all modules needed to run all the code
### tkinter for interactive windows
### matplotlib for plotting graphs
### csv to upload files 

import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
import numpy as np 

### making a tkinter window with the name 'welcome message' 
ws = Tk()
ws.title("Welcome message") 

### places a text box in the welcome message window displaying the text below
kj_label1 = Label(ws, text = "Please enter your name and click 'ok'")
kj_label1.pack()


### this function is called when the 'ok' buttn is clicked, displaying a set of messages using the input given above and displaying a new clickable button
def clicked1():
    msg = "\n" "Please click 'ready' to see your plot"
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Welcome, "+inp + msg)
    printButton2 = tk.Button(text = "ready", command = clicked2)
    printButton2.pack() 

### this function is called when the 'exit' button is clicked, will close the tkinter window
def clicked2():
    ws.destroy()

### dimensions and display of the input box 
inputtxt = tk.Text(width = 50, height=1)
inputtxt.pack()

### displays the clickable 'ok' button which will trigger the clicked1 function if clicked 
printButton1 = tk.Button( text = "ok", command = clicked1)
printButton1.pack() 

lbl = tk.Label(text = "")
lbl.pack()

ws.mainloop()

### opens a new tkinter window called pK plots 
ws = Tk()
ws.title("pK plots")


### this function is called when 'save' button is clicked 
def save_button():
     plt.savefig("output.jpg")

### this function is called when the 'about' button is clicked, opening a new tkinter window 
def clicked3():
    msg2 = "Hi!" "\n" "This application was made by Lot Burgstra, B914713. \nPlease, if you have any questions make sure to email me on: l.n.burgstra-19@student.lboro.ac.uk"
    ws = Tk()
    ws.title("About")
    kj_label3 = Label(ws, text = msg2)
    kj_label3.pack()

### creates a menubar with multiple attributes 
menubar = Menu(ws)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Save", command = save_button)
filemenu.add_separator()
filemenu.add_command(label= "Exit", command = clicked2)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "About", command = clicked3)
menubar.add_cascade(label = "Help", menu=helpmenu)

ws.config(menu = menubar)

### plots a graph with dimensions 12x8 with resolution 100
fig = plt.figure(figsize=(14,10), dpi=100)
plt1 = fig.add_subplot(111)

x = []
y = []
x1 = []
y1 = []

### files with data for the plots are loaded 
with open("pK2.csv", "r") as csvfile:
    lines = np.genfromtxt("pK2.csv", delimiter=",", dtype=None)
    for row in lines:
        x.append(row[0])
        y.append(row[1])

with open("pK3.csv", "r") as csvfile:
    lines = np.genfromtxt("pK3.csv", delimiter=",", dtype=None)
    for row in lines:
        x1.append(row[0])
        y1.append(row[1])

### both datasets are plotted as scatterplots on the same graph 
plt1.scatter(x,y,s = 20, c = 'b', marker='*', label = 'pK2')
plt1.scatter(x1,y1,s = 20, c = 'g', marker = '^', label = 'pK3')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), linestyle="--")
plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y1, 1))(np.unique(x1)), linestyle="--", color="green")

### any characteristics of the graph like axes titles, graph title and location of the legend 
plt.xlabel("log(VB/VA)")
plt.ylabel("pH")
plt.title("pH versus log(VB/VA) at different pK values")
plt.legend(loc='upper left')
plt.xlim([-1,1])
plt.ylim([5,11])
plt.text(0.50,7.2, "y = 1.0166x + 6.2324 \n R^2 = 0.9997", size=10, ha = "center", va="center", bbox=dict(boxstyle="round"))
plt.text(0.50, 10.5, "y = 1.0098x + 9.4739 \n R^2 = 0.9985", size=10, ha="center", va="center", bbox=dict(boxstyle="round"))
plt.minorticks_on()
plt.tick_params(which="major", width=1.5)
plt.tick_params(which="major", length=7)
plt.tick_params(which="minor", width=0.5, length=4, color="black")
plt.grid(True)


### adding the graph on a tkinter window 
scatter1 = FigureCanvasTkAgg(fig, ws)

scatter1.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)

ws.mainloop()
