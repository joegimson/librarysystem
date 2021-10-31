import sys
sys.path.append('coursework')

import database as d

while True:
    book= input ("Please enter the title of the book. If the result is empty the book is not in the system. Press q to exit:")
    if book =="q":
        break
    else:
        d.book_search(book)
    
    
