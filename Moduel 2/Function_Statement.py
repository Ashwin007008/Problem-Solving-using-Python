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
def display_invoice(username, amount, due_date):
    print(f"Hello{username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")    
display_invoice("Jhon", 230.04, "01/01")

#Return Statement:
# statement used to end a function and send a result back to the caller.
# z = add(1,2)  , result =3

def add(x, y):
    c = x + y
    return c
def Subtract(x, y):
    c = x - y
    return c
def Multiply(x, y):
    c = x * y
    return c
print(add(1,2))
print(Subtract(1,2))
print(Multiply(1,2))

# Example
def create_name(first, Last):
    first = first.capitalize()
    Last = Last.capitalize()
    return first + Last  # return first +" "+ Last
full_name = create_name("anba","sivam")
print(full_name)


