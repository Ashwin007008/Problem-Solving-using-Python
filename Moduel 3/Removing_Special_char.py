import re  # Import regex module

# Take input from the user
text = input()

# Remove all special characters (keep only letters)
clean_text = re.sub(r'[^a-zA-Z]', '', text)

# Print the result
print(clean_text)
"""

"""