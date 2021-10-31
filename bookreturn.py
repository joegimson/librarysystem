import sys
sys.path.append('coursework')

import database as d

while True:
    x = input("Please enter ID. press q to exit")
    if x == "q":
        break
    else:
        d.book_return(str(x))
    
    



            
            
