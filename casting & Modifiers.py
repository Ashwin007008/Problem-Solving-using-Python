#What is the Casting ?
#Casting means converting one data type into another data type.
#There are two types of casting in Python:
#1. Implicit Type Casting
a = 5
b = 2.0
c = a + b
print(c)
#2. Explicit Type Casting
x = "10"
y = int(x)
print(y)
m= 3.14
n = int(m)
print(n)
#What are Modifiers ?
#Modifiers are keywords that you can use to change the meaning of a variable or a function.
#There are two types of modifiers in Python:
#1. Global Modifier
x = 10
def func():
    global x
    x = 5
func()
print(x)
#2. Nonlocal Modifier
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()