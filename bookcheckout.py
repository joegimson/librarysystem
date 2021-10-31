import sys
sys.path.append('coursework')

import database as d

while True:
    bookID = input("Please enter ID. press q to exit:")
    memID= input("Enter 4 digit member ID:")
    if bookID == "q":
        break
    else:
        d.book_checkout(str(bookID), str(memID))
