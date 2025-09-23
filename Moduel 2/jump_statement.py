# Jump Statements
# Jump statements are used to alter the flow of control in a program.
# Python supports the following jump statements:
# 1. break statement
# 2. continue statement
# 3. pass statement
# 4. return statement
# 5. raise statement
# 6. yield statement
# 7. import statement
# 8. goto statement (not recommended) only in C++

# Example 1: Using break statement in a loop
count = 0
while True:  # acts like 'do'
    count += 1
    print("Count is:", count)
    if count >= 5:
        break
#########################################################################################################################################################################
# Example 2: Using continue statement in a loop
count = 0
while count < 10:  # Loop until count is less than 10
    count += 1     # Increment count
    if count % 2 == 0:  # Skip even numbers
        continue
    print("Odd Count is:", count)
#########################################################################################################################################################################
# Example 3: Using pass statement
for i in range(5): # Loop from 0 to 4
    if i == 3:     # Placeholder for future code
        pass       # Do nothing, where pass is used as a placeholder for future code
    else:         # This block will execute for all other values of i
        print("Value is:", i)

    
#########################################################################################################################################################################
# Example 4: Using return statement in a function
def add(a, b):     # Function to add two numbers
    return a + b   # Return the sum
result = add(5, 3)  # Call the function
print("Sum is:", result)
#########################################################################################################################################################################
# Example 5: Using raise statement to throw an exception
def divide(a, b):   # Function to divide two numbers
    if b == 0:       # Check for division by zero
        raise ValueError("Cannot divide by zero")  # Raise an exception
    return a / b  # Return the result
# Test the function
try:    # Handle potential exception, means try to execute the code, try stand is used to catch the exception
    result = divide(10, 0)  # This will raise an exception
    print("Result is:", result)  # This line will not execute
except ValueError as e:   # Catch the exception and print the error message
    print("Error:", e)   # Print the error message
#########################################################################################################################################################################
# Example 6: Using yield statement in a generator function
def count_up_to(n):    # Function to count up to a given number
    count = 1          # Initialize count
    while count <= n:  # Loop until count exceeds n
        yield count    # Yield the current count
        count += 1     # Increment count
for number in count_up_to(5):  # Iterate through the generator
    print("Generated number:", number)   # Print each generated number
#########################################################################################################################################################################
# Example 7: Using import statement to include a module
import math   # Import the math module
print("Square root of 16 is:", math.sqrt(16))  # Use the sqrt function from the math module
#########################################################################################################################################################################
# Example 8: Using goto statement (not recommended)
# Python does not have a built-in goto statement, but you can simulate it using exceptions or functions.
# However, using goto is generally discouraged as it can lead to unstructured and hard-to-read code.