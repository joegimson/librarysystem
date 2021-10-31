from tkinter import *

import sys
sys.path.append('coursework')

import database as d

def exitwindow():
    window.destroy()



window=Tk()
window.title("Library Management System")
window.geometry("500x120")

btnSearchBooks=Button(window,text = "Search Books",
                      command = lambda:d.book_search(txtbook.get()))
btnBookCheckout = Button(window, text = "Checkout Book",
                         command = lambda:d.book_checkout(txtbookID.get(), txtmemberID.get()))
btnBookReturn = Button(window, text = "Return Book",
                       command = lambda:d.book_return(txtbookID2.get()))
btnBye = Button(window, text = "Exit",
                command = exitwindow)


lblbook = Label(window, text = "Enter Book:")
txtbook= Entry(window, width=20)

lblbookID = Label(window, text = "Enter ID:")
txtbookID = Entry(window, width = 15)
lblmemberID = Label(window, text = "Enter 4 digit Member ID:")
txtmemberID = Entry(window, width = 5)

lblbookID2 = Label(window, text = "Enter ID:")
txtbookID2 = Entry(window, width = 15)

btnSearchBooks.grid(column=2, row=0)
lblbook.grid(column = 0, row = 0)
txtbook.grid(column = 1, row = 0)

btnBookCheckout.grid(column = 4, row = 1)
lblbookID.grid(column=0, row =1)
txtbookID.grid(column = 1, row =1)
lblmemberID.grid(column = 2, row =1)
txtmemberID.grid(column =3, row = 1)

btnBookReturn.grid(column = 2, row = 2)
lblbookID2.grid(column = 0, row = 2)
txtbookID2.grid(column = 1, row =2)

btnBye.grid(column = 0, row = 3)

window.mainloop()
