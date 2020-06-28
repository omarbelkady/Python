import tkinter as tk
from tkinter import filedialog, Text 
import os 
#tkinter for creation of the GUI
#filedialog:for filing the apps
#Text: displaying text
#os: allows us to run the apps that we will add to our app

#Create an apps array that will apppend all the files that were added to the implementMyApp function




root= tk.Tk() #root holds the whole structure of our app




myApp=[]

#Right after closing the app there is a comma generated I want to remove that
#I am going to load the text file

if os.path.isfile('save.txt'):
	with open('save.txt','r') as f:
        temporApp=f.read()
        temporApp=temporApp.split(',')
        myApp=[o for o in temporApp if o.strip()]
        


#GIVING ACTION TO OUR BUTTONS, open the app, clicking it and save it and close
def implementMyApp():#addApp
    #if a label is attached delete it
    for widget in myFrame.winfo_children():
        widget.destroy()
        
    
    myFileName=filedialog.askopenfilename(myinitialdir="/", title= "Choose File",#filename
    filetyp=(("executables", "*.exe"), ("all files", "*.*")))
    #myinitialdir= initialdir
    myApp.append(myFileName)
    print(myFileName)
    
    #We will now loop through the myApp list/array to print out what we have within the array
    #This file should be named theapp.py
    for theapp in myApp:
        label=tk.Label(myFrame, text=theapp, bg="grey")
        label.pack()#the pack function attaches the file to the screen

#We need to run the app runApps=runTheApp
def runTheApp():
    for theapp in myApp:
        os.startfile(theapp)
        


#To make bigger we will create a canvas
#for the input we put where we want to attach the Canvas
#bg stands for background
myCanvas= tk.Canvas(root, height=701, width=701, bg="#263D42")

#To attach the the canvas to the root
myCanvas.pack()

#To attach say a div like a container
myFrame=tk.Frame(root, bg="white")


#To place the Frame
#myFrame.place(relwidth= 0.7, relheight=0.7)

#To center the Frame
myFrame.place(relwidth=0.7,relheight=0.7, relx=0.2, rely=0.2)

#I want to add a button to the app
openFile=tk.Button(root, text="Open My File Please", padx= 9, pady= 4.5, fg="blue", bg="#263D42" command = implementMyApp)

#Now I have to attach the File
openFile.pack()


#I want to add a button to launch the app
runTheApp=tk.Button(root, text="Launch", padx= 9, pady= 4.5, fg="blue", bg="#263D42", command=runTheApp)

#Now I have to attach the button to the root
runTheApp.pack()


#To display the attached image even after I close the application
for app in myApp:
    label=tk.Label(myFrame, text=app)
    label.pack()

root.mainloop()

with open("save.txt","w") as f:
    for theapp in myApp:
        f.write(theapp + ",")
