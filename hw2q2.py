#Assignments: Tuples
'''
2. Python Data Structure Challenges in Real-World Scenarios

Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

'''
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
tup = ()
s = 0

def add(x, y):
    listn = []
    listn.append(x)
    listn.append(y)
    tn = ()
    tn = tuple(listn)
    return tn

print("Welcome to the Library System Enhancement!")
print("Please update this system by adding new books and no duplicates.")
print("Menu:")
print("1. View Current Library System.")
print("2. Add new book with Date.")
print("3. To Quit")
#User Interaction
try:
      x = ""
      y = ""
      ticketn = ""
      while(s != 3):
        s = int(input("Please enter a number 1 - 3 of what you want to do by looking at the Menu: "))
        if(s == 1):
             print("The Current Library System is printed below.")
             print(library)
        elif(s == 2):
             x = input("Please enter the Title of the Book, Example - 1984 or Brave New World: ")
             y = input("Please enter the Author of the Book, Example - George Orwell or Aldous Huxley: ")   
             print("Checking if values entered already exist in library... ")

             for t in library:
                  if x in t:
                       print("NO Duplicates allowed. Please Try Again")
                       exit()
                  if y in t:
                       print("NO Duplicates allowed. Please Try Again")
                       exit()
             
             tup = add(x, y)
             library.append(tup)
             print("The values are not duplicates so they have been added to the Library System.")
                        
        elif(s == 3):
             print("Thank You for using this  Library System Enhancement application. GoodBye!")
             break
        else:
             print("Please enter a number 1 - 3. Please Try Again")
             break                           
      
except ValueError:
      #Code to handle incorrect input type
      print("Please enter a valid integer.")
except Exception as e:
      #Code to handle an unexpected exception
      print(f"An unexpected error occured: {e}")
else:
      pass
finally:
        print("Thank you for your response.")
