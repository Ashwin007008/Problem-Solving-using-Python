pos = -1 # Global variable to store position of found element

def search(list, n):                         # Function to search for n in list
    i = 0                                    # Initialize index
    while i < len(list):                     # Loop through the list
        if list[i] == n:                     # If element is found
            globals()['pos'] = i             # Update global position variable
            return True                      # Return True if found
        i = i + 1                            # Increment index
    return False                             # Return False if not found

list = [10, 20, 30, 40, 50]                  # Sample list
n = 30                                       # Element to search for
if search(list, n):                          # Call the search function
    print("Found at", pos + 1)               # Print position (1-based index)
else:                   
    print("Not Found")   
