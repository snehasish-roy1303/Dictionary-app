from tkinter import *
import dict
window = Tk()

window.title('Dictionary')

def search():
    r = dict.search_meaning(e1_Value.get())
    lis.delete(0, END)
    lis.insert(END, r)

L1 = Label(window, text='Word')
L1.grid(row=0, column=0)
L2 = Label(window, text='Meaning')
L2.grid(row=1, column=0)

e1_Value = StringVar()
e1 = Entry(window, textvariable=e1_Value)
e1.grid(row=0, column=1)

b1 = Button(window, text='Find', width=12, command=search)
b1.grid(row=2, column=1)
b2 = Button(window, text='Close', width=12, command=window.destroy)
b2.grid(row=3, column=1)

lis = Listbox(window, height=6, width=30)
lis.grid(row=2, column=0, rowspan=5, columnspan=1)

s=Scrollbar(window, orient='horizontal')
s.grid(row=8,column=0,rowspan=200)

lis.configure(xscrollcommand=s.set)
s.configure(command=lis.xview)

window.mainloop()
