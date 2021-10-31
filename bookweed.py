import matplotlib.pyplot as plt

import sys
sys.path.append('coursework')

import database as d


newlist = [j for i, j in enumerate(d.logfile_list()) if i not in [0, 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50, 52, 53, 55, 56]] #creates a list with just ISBN
newerlist = ([[x,newlist.count(x)] for x in set(newlist)]) #creates a list of list of all ISBN and number of times they appear in logfile.txt
print ("The ISBN with the lowest amount of times loaned out should be deleted.")


x = tuple(map(lambda x: x[0], newerlist)) #puts ISBNs in a new list which is converted to a tuple
y = tuple(map(lambda x: x[1], newerlist)) #puts amount of times corresponding ISBN appears into a list and is converted to a tuple
plt.xlabel('ISBN')
plt.ylabel('Amount of time book has been loaned out')
plt.title('ISBN and amount of times they have been loaned out and returned')
plt.bar(x, y)
plt.show()

