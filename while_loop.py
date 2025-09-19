#What Is a While Loop
count = 10              # Initialize a counter variable
while count <= 50:       # Loop condition: repeat while count is less than or equal to 5
    print(count)        # Print the current value of count
    count += 10          # Increase the count by 1 after each loop iteration

############################################################################################################
i = 1
while i <= 5:      #Outer while loop controls the rows (from 1 to 5).
    j = 1
    while j <= i:   #Inner while loop prints the current row number i exactly i times on the same line.
        print(i, end=" ")
        j += 1
    print()  # Move to next line after each row
    i += 1

#############################################################################################################
n = int(input("Enter number of rows: "))  # User input for number of rows

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()  # New line after each row
    i += 1

################################################################################################################
n = int(input("Enter number of rows: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
    """
*
* *
* * *
* * * *
* * * * *
    """