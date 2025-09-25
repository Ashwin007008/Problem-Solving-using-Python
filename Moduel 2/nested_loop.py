# Nested Loop
"""
 Nested loops are loops within loops. 
 The "inner loop" will be executed one time for each iteration of the 
 "outer loop".
"""

#########################################################################################################################################################################
# Example 1: Nested for loop
for i in range(1, 6):  # Outer loop
    for j in range(3):  # Inner loop
        print(f"i: {i}, j: {j}") # Print current values of i and j
    print("End of inner loop for i =", i) # Indicates end of inner loop
print("End of outer loop") # Indicates end of outer loop

#########################################################################################################################################################################
# Example 2: Print a pattern using nested loops
n = 5  # Number of rows
for i in range(1, n + 1):       # Outer loop for rows
    for j in range(1, i + 1):   # Inner loop to print numbers in each row
        print(j, end=" ")       # Print number j with space, no new line
    print()                     # Move to the next line after each row