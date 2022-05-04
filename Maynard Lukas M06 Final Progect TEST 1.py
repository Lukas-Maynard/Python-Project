"""
M06 Final Project TEST 1
Lukas Maynard
SDEV-140
description
"""
from tkinter import *
root = Tk()
root.title('Final Project')

def header():
    homeButton = Button(root, text='Home', command=page1)
    homeButton.grid(row=0, column=0, padx=10, pady=5)

    settingsButton = Button(root, text='Settings', command=pageSettings)
    settingsButton.grid(row=0, column=1,padx=10, pady=5)

def page1():
    pageSettings.quit()
    header()
    pageId = Label(root, text='Page 1',)
    pageId.grid(row=2, column=0, padx=10, pady=5)

def pageSettings():
    page1.quit()
    header()
    pageId = Label(root, text='Settings page',)
    pageId.grid(row=2, column=0, padx=10, pady=5)

def main():
    page1()
    root.mainloop()

if __name__ == '__main__':
    main()
