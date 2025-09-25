# This is a simple do-while loop in Python
count = 0
while True:   # why True: creates an infinite loop, simulating do-while
    count += 1
    print("Count is:", count)
    if count >= 5:
        break
    
#########################################################################################################################################################################
# Multiplication table using do-while style in Python

n = int(input("\nExample 2:Enter a number: "))

i = 1
while True:  # acts like 'do'
    print(n * i, end=" ")
    i += 1
    if i > 10:  # exit condition like 'while (i <= 10)'
        break

    
#########################################################################################################################################################################
# Example 3: Checking if a number is even or odd do-while style

num = int(input("\nExample 3:Enter a number: "))  # Take number input from user
while True:   # Simulating do-while loop
    if num % 2 == 0: # Check if the number is even
        print("Even number")
    else:
        print("Odd number")
    # Ask the user if they want to check another number
    choice = input("Do you want to check another number? (yes/no): ").strip().lower() # Normalize input
    if choice != 'yes': #choice is not yes then 
        break
    num = int(input("Enter a number: "))  # Take new number input from user

#########################################################################################################################################################################
# Example 4: Simple password check do-while style
correct_password = "letmein"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Access denied")

#########################################################################################################################################################################
# Example 5: Simple menu-driven program
while True:
    print("\nMenu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    choice = input("Choose an option (1-3): ").strip()
    
    if choice == '1':
        print("You chose Option 1")
    elif choice == '2':
        print("You chose Option 2")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")
year = int(input("Example 5:Enter a year: "))  # Take year input from user
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")  # Nested: check for leap year
else:
    print("Not a leap year")  # Nested: not a leap year 


#########################################################################################################################################################################

# Dictionary operator in do-while style loop

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Cannot divide by zero"

operations = {
    '1': add,
    '2': sub,
    '3': mul,
    '4': div
}

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == '5':
        print("Exiting the program.")
        break
    if choice in operations:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        result = operations[choice](x, y)
        print("Result:", result)
    else:
        print("Invalid choice, please try again.")