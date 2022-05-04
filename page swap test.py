from tkinter import *
root = Tk()
root.title('page 1')
root.geometry('400x400')

# def page1():
#     label = Label(root, text='this is page 1')
#     label.grid(row=0, column=0, padx=10, pady=10)
#     button = Button(root, text= 'go to page 2', command=page2)
#     button.grid(row=1, column=0, padx=10, pady=10)

# def page2():
#     label = Label(root, text='this is page 2')
#     label.grid(row=0, column=0, padx=10, pady=10)
#     button = Button(root, text= 'go to page 1', command=page1)
#     button.grid(row=1, column=0, padx=10, pady=10)

class Page:
    def defaultPage():
        label = Label(root, text='this is page 1')
        label.grid(row=0, column=0, padx=10, pady=10)
        button = Button(root, text= 'go to page 2', command=Page2.page2())
        button.grid(row=1, column=0, padx=10, pady=10)

class Page2(Page):
    def page2():
        button = Button(root, text='go to page 3', command=Page3)

class Page3(Page):
    def page3():
        button = Button(root, text='back to page 1', command=Page)


def main():
    Page.defaultPage()
    root.mainloop()


if __name__ == '__main__':
    main()
