"""
M06 Final Project TEST #2
Lukas Maynard
SDEV-140
A personalized text TextBox with the ability to make and save new files. Capable of multiple tabs

- could use paned windows to get row numbers?
- focus on adding the file editing, opening, and saving
- make resizing better
"""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

# make list for textboxes that uses the same index as the tabs -- requires some rewriting
# Fix aspect ratios and make resisability better

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title('Text Editor')
        self.root.geometry("1200x660")

        self.topmenu = Menu(self.root)
        self.root.config(menu=self.topmenu)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack()

        self.filetypes = [('Text Files', '*.txt'),('Python Files', '*.py'),('All Files', '*.*')]

        self.count = -1
        self.tabList = []

        # Highlighted text used for edit menu
        self.selected = False

        # Top FILE Menu
        self.filemenu = Menu(self.topmenu, tearoff=False)
        self.topmenu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='New File', command=self.NewFile)
        self.filemenu.add_command(label='Open', command=self.OpenFile)
        self.filemenu.add_command(label='Save As', command=self.SaveAsFile)
        # self.filemenu.add_command(label='Save', command=self.SaveFile)        
        self.filemenu.add_command(label='Close File', command=self.CloseFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.root.quit)

        # Top EDIT Menu
        self.editmenu = Menu(self.topmenu, tearoff=False)
        self.topmenu.add_cascade(label='Edit', menu=self.editmenu)
        self.editmenu.add_command(label='Cut       (Ctrl+x)', command=lambda: self.CutText(False))
        self.editmenu.add_command(label='Copy    (Ctrl+c)', command=lambda: self.CopyText(False))
        self.editmenu.add_command(label='Paste    (Ctrl+v)', command=lambda: self.PasteText(False))
        # self.editmenu.add_command(label='Undo   (Crtl+z)')
        # self.editmenu.add_command(label='Redo   (Crtl+Shift+z)')

        # Matching Keybinds to edit menu
        root.bind('Control-x', self.CutText)
        root.bind('Control-c', self.CopyText)
        root.bind('Control-v', self.PasteText)

        # Top SETTINGS Menu
        self.settingsmenu = Menu(self.topmenu, tearoff=False)
        self.topmenu.add_cascade(label='Settings', menu=self.settingsmenu)
        # self.settingsmenu.add_command(label='Color Mode', command=self.ColorToggle)

        # Bottom STATUS Bar
        self.status = Label(root, text='Welcome', anchor=W)
        self.status.pack(fill=X, side=BOTTOM, padx=8, ipady=5)


    def NewTab(self):
        """ Create Frames and place them in Tabs, Organized in a list """
        self.count += 1
        self.tabList.append(f'newFileFrame{self.count}')
        self.tabList[self.count] = Frame(self.notebook, width=1200, height=660, bg='white')

    def NewFile(self):
        """ Uses NewTab() and inserts the textbox/scrollbar, Adds it into the tablist """
        self.NewTab()
        self.tabList[self.count].pack(fill='both', expand=1)
        self.notebook.add(self.tabList[self.count], text=f'Tab {self.count + 1}')
        # Create Scrollbar
        TextScroll = Scrollbar(self.tabList[self.count])
        TextScroll.pack(side=RIGHT, fill=Y)
        # Create Text Box
        self.TextBox = Text(self.tabList[self.count], width=95, height=29, font=('Lucida Console', 16), selectbackground="grey", selectforeground="black", undo=True, yscrollcommand=TextScroll.set)
        self.TextBox.pack()
        # Configure Scrollbar
        TextScroll.config(command=self.TextBox.yview)
        self.status.config(text='New File Created')

    def OpenFile(self):
        """ Uses NewFile() and places chosen file in to textbox """
        textfile = filedialog.askopenfilename(initialdir=os.getcwd(), title='Open File', filetypes=self.filetypes)
        filename = textfile.replace('C:/','')
        self.status.config(text=filename)
        # Can reuse the NewFile method here!
        self.NewFile()
        # Putting the chosen file in TextBox -- Made TextBox available to the rest of the class to make this work.
        textfile = open(textfile, 'r')
        content = textfile.read()
        self.TextBox.insert(END, content)
        textfile.close

        self.status.config(text='File Opened')
        ## FIX ##--> Not selecting a file to open doesnt make a new tab

    def SaveAsFile(self):
        """ Saves the file -- Needs fix currently only saves last file in list """
        # currenttab = self.tabList[self.notebook.index(self.notebook.select())]
        textfile = filedialog.asksaveasfilename(defaultextension='.*', initialdir=os.getcwd(), title='Save File', filetypes=self.filetypes)
        if textfile:
            filename = textfile.replace('C:/','')
            self.status.config(text=filename)

            textfile = open(textfile, 'w')
            # Needs fixing to save correct tab -- currently only save last tab
            textfile.write(self.TextBox.get(1.0, END))
            textfile.close

    def SaveFile(self):
        pass
    # https://www.youtube.com/watch?v=yG0fAUn2uB0

# Change this for only the needed widgets being deleted --- Small Bug Fix Needed ---
    def CloseFile(self):
        """ Closes the currently opened tab - Destroys all contents inside instead of keeping them in memory """
        for widget in self.tabList[self.notebook.index(self.notebook.select())].winfo_children():
            widget.destroy()
            self.tabList[self.notebook.index(self.notebook.select())].pack_forget()
        self.notebook.forget(self.notebook.index(self.notebook.select()))
        self.count -= 1
        self.status.config(text='Closed File')

    # This will be the user manual/help page (w/2 images) (Put in file menu)
    # def UserManual():
        # pass

    def CutText(self, e):
        """ Accessibility option for Cutting text """
        # Check if keyboard shortcut is used (using Lambda function)
        if e:
            self.selected = self.root.clipboard_get()
        else:
            if self.TextBox.selection_get():
                self.selected = self.TextBox.selection_get()
                self.TextBox.delete('sel.first', 'sel.last')
                self.root.clipboard_clear()
                self.root.clipboard_append(self.selected)

    def CopyText(self, e):
        """ Accessibility option for Copying text """
        # Check if keyboard shortcut is used (using Lambda function)
        if e:
            self.selected = self.root.clipboard_get()
        else:
            if self.TextBox.selection_get():
                self.selected = self.TextBox.selection_get()
                self.root.clipboard_clear()
                self.root.clipboard_append(self.selected)

    # Pasteing is slightly buggy when a keybind is used to get text first  -- Recomend just using normal keybord shortcuts 
    # Also buggy throughout multiple tabs -- Textbox list would be needed to help this issue
    def PasteText(self, e):
        """ Accessibility option for Pasteing text """
        # Check if keyboard shortcut is used (using Lambda function)
        if e:
            self.selected = self.root.clipboard_get()
        else:
            if self.selected:
                cursorPosition = self.TextBox.index(INSERT)
                self.TextBox.insert(cursorPosition, self.selected)

def main():
    root = Tk()
    TextEditor(root)
    # Could start app with a new file opened by using the next line in trade for the one above
    #TextEditor(root).NewFile()
    root.mainloop()

if __name__ == '__main__':
    main()
