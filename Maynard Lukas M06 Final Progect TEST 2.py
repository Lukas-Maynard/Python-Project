"""
M06 Final Project TEST #2
Lukas Maynard
SDEV-140
This will be a personalized text editor with the ability to make and save new files.

--CURRENT!!: Working "New file" button and "Exit" button -- Top Menu stays on screen when new frame is made.
"""
from tkinter import *
root = Tk()
root.title('Final Project')
root.geometry('400x400')
# Create top menu
TopMenu = Menu(root)
root.config(menu=TopMenu)

def NewFile():
    newFileFrame.pack(fill='both', expand=1)

def ModeToggle():
    #This will be a Dark/Light Mode toggle in settings menu
    pass

# Create menu items
FileMenu = Menu(TopMenu)
TopMenu.add_cascade(label='File', menu=FileMenu) 
FileMenu.add_command(label='New', command=NewFile)
FileMenu.add_separator()
FileMenu.add_command(label='Exit', command=root.quit)

#Create Settings Menu
EditMenu = Menu(TopMenu)
TopMenu.add_cascade(label='Settings', menu=EditMenu)
EditMenu.add_command(label='Dark/Light Mode Toggle', command=ModeToggle)

# Creating Frames
newFileFrame = Frame(root, width=400, height=400, bg='red')


def main():
    root.mainloop()

if __name__ == '__main__':
    main()
