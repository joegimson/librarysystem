def book_search(book):
    """
This function asks the user to search for a book and if the book is in database.txt prints the corresponding line(s).

    """
    with open("database.txt", "r") as search:
        for line in search:
            if book in line:
                print (line)
    search.close()

def read_books():
    """
This function puts all elements of database.txt into a list and is used for bookcheckout and bookreturn.

    """
    booklist = []
    f = open("database.txt", "r")
    x = f.readlines()
    for book in x:
        cleanbook = book.strip()
        books = cleanbook.split("\t")
        booklist.append(books)
    onelist = []
    for sublist in booklist:
        for item in sublist:
            onelist.append(item)
    return onelist
    f.close()

def book_checkout(ID, memberID):
    """
This function asks for the ID of the book and if member ID of the book is equal to zero the new member ID
is written into the database.

    """
    if str(ID) in read_books():
        ID_pos = read_books().index(str(ID)) #finds index of the users inputted ISBN
        memberID_pos = read_books()[ID_pos + 5]
        if memberID_pos == '0':
                goodlist = read_books()
                goodlist[ID_pos+5] = str(memberID)
                w = open("database.txt", "w")
                new_file_contents = "\t".join(goodlist)
                w.write(new_file_contents)
                w.close()
                print ("Book successfully checked out.")
                fix_database() 
                
        else:
            print("This book is already taken.")
    else:
        print("Book ID incorrect.")

def fix_database():
    """
This function is used to fix the database.txt file after a book is checked out or returned.

    """
    thelist = read_books()
    thelist[6] = '\n' + '2'
    thelist[12] = '\n' + '3'
    thelist[18] = '\n' + '4'
    thelist[24] = '\n' + '5'
    thelist[30] = '\n' + '6'
    thelist[36] = '\n' + '7'
    thelist[42] = '\n' + '8'
    thelist[48] = '\n' + '9'
    thelist[54] = '\n' + '10' #new line of text should be added if a new book is added to the database in format thelist[x+6] = '\n' +'a+1' where x is the number on the last line of code. If a book is removed the last line must be deleted.   
    v = open("database.txt", "w")
    output = '\t'.join(thelist)
    v.write(output)
    v.close()
    readable_v = open("database.txt", "r")
    read_v = readable_v.read()
    print (read_v) # prints content of fixed database

def book_return(ID):
    """
This function asks for the ID and sets member ID to 0 if the book copy's member ID isn't equal to 0.

    """
    if str(ID) in read_books():
        ID_pos = read_books().index(str(ID))
        memberID_pos = read_books()[ID_pos + 5]
        if memberID_pos != '0':
            newlist = read_books()
            newlist[ID_pos + 5] = '0'
            w = open("database.txt", "w")
            new_file_content = "\t". join(newlist)
            w.write(new_file_content)
            w.close()
            print ("Book successfully returned.")
            fix_database()
        else:
            print("This book is already returned.")
    else:
        print("Book ID incorrect.")


def logfile_list():
    """
This function puts all elements of logfile.txt into a list. This function is used for book weeding.

    """
    loglist = []
    f = open("logfile.txt", "r")
    x = f.readlines()
    for item in x:
        cleanitem = item.strip("\n") 
        items = cleanitem.split("\t")
        loglist.append(items)
    onelist = []
    for sublist in loglist:
        for item in sublist:
            onelist.append(item)
    return onelist
    f.close()
