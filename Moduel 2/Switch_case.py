#Swich Case
"""What is Switch Case?
A switch case is a control statement that allows a variable 
to be tested for equality against a list of values.
Each value is called a case, and the variable being switched 
on is checked for each case.

there are two ways to implement switch-case in Python:
1. Using List statements
2. Using dictionary mapping (which is a more Pythonic way)"""

#List Statement { Not for LU}
def getInput():
    a = int(input("Enter Frist Number: "))
    b = int(input("Enter Second Number: "))
    return a, b 
def add():
    x,y = getInput()
    return x + y
def Sub():
    x,y = getInput()
    return x - y
def Mult():
    x,y = getInput()
    return x * y
def div():
    x,y = getInput()
    return x // y
print("""
    1.Add
    2.Sub
    3.Mult
    4.Div
""")
choice = int(input("Enter Your Choice:  "))

operations = [add, Sub, Mult, div]  #[0, 1, 2, 3]

if 1 <= choice <= 4:
    output = operations[choice - 1]()
    print("Result:", output)
else:
    print("Invalid choice")



#################################################################################################################################################################################################

def switch_case_example(value):   #def is a keyword to define a function, value is a parameter
    switcher = {
        1: "You selected option 1",
        2: "You selected option 2",
        3: "You selected option 3"
    }
    return switcher.get(value, "Invalid option")

# Taking input from user
print("Example 1")
option = int(input("Enter an option (1-3): "))
result = switch_case_example(option)
print(result)
#########################################################################################################################################################################
# Example 2: Simple calculator using switch-case
def calculator(num1, num2, operation):
    operations = {
        'add': num1 + num2,
        'subtract': num1 - num2,
        'multiply': num1 * num2,
        'divide': num1 / num2 if num2 != 0 else "Cannot divide by zero"
    }
    return operations.get(operation, "Invalid operation")
# Taking input from user
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
op = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
calc_result = calculator(number1, number2, op)
print(calc_result)
#########################################################################################################################################################################
# Example 3: Day of the week using switch-case
def day_of_week(day_num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day_num, "Invalid day number") #.get 
# Taking input from user
day_number = int(input("Enter a day number (1-7): "))
day_name = day_of_week(day_number)
print(day_name)
#########################################################################################################################################################################
# Example 4: Grade evaluation using switch-case
def grade_evaluation(grade):
    grades = {
        'A': "Excellent",
        'B': "Good",
        'C': "Average",
        'D': "Below Average",
        'F': "Fail"
    }
    return grades.get(grade.upper(), "Invalid grade")
# Taking input from user
user_grade = input("Enter your grade (A-F): ").strip().upper()
evaluation = grade_evaluation(user_grade)
print(evaluation)
#########################################################################################################################################################################
# Example 5: Month name using switch-case
def month_name(month_num):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months.get(month_num, "Invalid month number")
# Taking input from user
month_number = int(input("Enter a month number (1-12): "))
month = month_name(month_number)
print(month)
#########################################################################################################################################################################
# Example 6: Traffic light color using switch-case
def traffic_light(color):
    colors = {
        'red': "Stop",
        'yellow': "Caution",
        'green': "Go"
    }
    return colors.get(color.lower(), "Invalid color")
# Taking input from user
light_color = input("Enter traffic light color (red, yellow, green): ").strip().lower()
action = traffic_light(light_color)
print(action)
#########################################################################################################################################################################
# Example 7: Simple menu selection using switch-case
def menu_selection(choice):
    menu = {
        1: "Pizza",
        2: "Burger",
        3: "Pasta",
        4: "Salad"
    }
    return menu.get(choice, "Invalid choice")
# Taking input from user
menu_choice = int(input("Enter your menu choice (1-4): "))
selected_item = menu_selection(menu_choice)
print(selected_item)
#########################################################################################################################################################################