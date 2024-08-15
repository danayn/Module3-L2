#Assignments: Tuples
'''
1. Tuple Mastery in Python

Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument.
Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
The function should format and return a string that lists each itinerary.
For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"

'''
input1 = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

result = "Itinerary "
count = 0


def itinerary(fl_input, count, result):
   c = 0
   count = count + 1
   for i in fl_input:
      c = c + 1
      if(c == 1):
         result = result + str(c)
         result = result + ": "
         result = result + i + " - "
      if(c == 2):
         result = result + "From "
         result = result + i
      if(c == 3):
         result = result + " to "
         result = result + i

         print(result)



for i in input1:
   itinerary(i, count, result)

