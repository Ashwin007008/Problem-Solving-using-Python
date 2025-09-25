"""
What is function
                 function = A block of reusable code

                 place () after the function name to invoke it
                 """

def happy_birthday():
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday to you")
   

happy_birthday()  

def happy_birthday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print(f"Happy birthday to {name}") # F
   

happy_birthday("Player 1")
happy_birthday("Player 23")
happy_birthday("Player 208")



def happy_birthday(name, age):
    print("Happy birthday to you")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}")
   

happy_birthday("Ram", 23)
happy_birthday("Jhon", 8)
happy_birthday("Raj ", 15)

#Example for function:
def display_invoice(username, amount, due_date): # Function with parameters
    """Function to display an invoice"""
    print(f"Hello {username}") # Using f-string for formatting
    print(f"Your bill of ${amount:.2f} is due: {due_date}") # Format amount to 2 decimal places
display_invoice("Jhon", 230.04, "01/01") # Call the function with arguments
display_invoice("Ram", 450.78, "05/01") # Call the function with different arguments
display_invoice("Raj", 120.50, "10/01") # Call the function with different arguments

#Return Statement:
# statement used to end a function and send a result back to the caller.
# z = add(1,2)  , result =3

def add(x, y):
    c = x + y
    return c # return x + y
def Subtract(x, y):
    c = x - y
    return c # return x - y
def Multiply(x, y):
    c = x * y
    return c # return x * y
print(add(1,2)) # 3
print(Subtract(1,2)) # -1
print(Multiply(1,2)) # 2 

# Example
def create_name(first, Last):
    first = first.capitalize()
    Last = Last.capitalize()
    return first +" "+ Last  # Concatenate first and last name
full_name = create_name("anba","sivam")
print(full_name)


