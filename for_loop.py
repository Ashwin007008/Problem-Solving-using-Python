#For loop function
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)

#Example 1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Example 2
n = int(input())
 
for i in range(1, n + 1):
    print(i, end=",")
"""
Step 1: Get Input and Convert to Number
n = int(input())
    This asks the user to type a number and press Enter.
    input() reads what the user types (as text).
    int(...) changes that text to an integer (whole number), storing it in the variable n.

Step 2: For Loop Setup
for i in range(1, n + 1):
    This starts a loop that goes from 1 up to, and including, n.
    The range(1, n + 1) function gives all numbers starting at 1 and ending at n.
    i is a variable that will take on each value in this range, one at a time.

Step 3: Display Each Number
print(i, end=",")

Inside the loop, print(i, end=",") writes the current number on the screen, 
followed by a comma instead of a new line.
This means all numbers print side by side, separated by commas.

Example Output
If a user enters 5, this will be printed:
"""

#Example 3
n = 5  # Number of rows

for i in range(1, n + 1):       # Outer loop for rows
    for j in range(1, i + 1):   # Inner loop to print numbers in each row
        print(j, end=" ")       # Print number j with space, no new line
    print()                     # Move to the next line after each row