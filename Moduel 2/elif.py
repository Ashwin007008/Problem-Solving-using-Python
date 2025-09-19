"""
Examples of elif statements in Python   
library fine problem
Days late     Fine
0              $0
1  - 5         $1
6  - 12        $3
13 - 19        $5
20 or more     membership cancelled     

"""
days= int(input("Enter the number of days the book is late: "))
if days == 0:
    fine = 0
elif 1 <= days <= 5:
    fine = 1
elif 6 <= days <= 12:
    fine = 3
elif 13 <= days <= 19:
    fine = 5
else:
    fine = "Membership cancelled"