
#If and Else Statements


######################################################################
#Example 1: Check if a number is positive or negative

print("Example 1: Check if a number is positive or negative")

number = float(input("Enter a number: "))
if number >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")

#####################################################################
#Example 2: Determine if a person is eligible to vote

print("Example 2: Determine if a person is eligible to vote")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are ", age,"eligible to vote.")
else:
    print("You are ", age,"not eligible to vote.")





#########################################
#Example 3: Check Weather Condition
weather = input("Enter the weather (sunny/rainy/cloudy): ").strip().lower()
if weather == "sunny":
    print("It's a sunny day! Wear sunglasses.")
elif weather == "rainy":
    print("It's a rainy day! Don't forget your umbrella.")
else:
    print("It's a cloudy day! Dress comfortably.")
    
