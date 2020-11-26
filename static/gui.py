from tkinter import *
from tkinter.ttk import *

# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 

root = Tk()
root.geometry('200x100')

# This function will be used to open 
# file in read mode and only Python files 
# will be opened 

line = ""

def open_file():
    file = askopenfile(mode ='r', filetypes =[('Text', '*.txt')]) 
    if file is not None:
        content = file.read()
        line = content
        print(line)

btn = Button(root, text ='Open', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10) 

mainloop() 

