"""What Are Control Structures?

Control structures manage how your program flows:

The order of statements.

Whether a block runs or not.

How many times a block repeats.

They give your program the ability to think, choose, and loop."""

#1.Sequential Control Structure

# (Start) → [Step 1] → [Step 2] → [Step 3] → (End)
print("Example of Sequential Control Structure")
print("Open the fridge")
print("Take out the milk")
print("Pour into glass")
print("Drink the milk")

################################################################

"""2.Selection Control Structure
        [Condition?]
        /        \
     True        False
     /              \
 [Do this]       [Do that]
"""
print("Example of Selection Control Structure")
number = 5
if number > 0:
    print("Positive")
else:
    print("Zero or Negative")

################################################################

"""3. Iteration (Looping) Control Structure
      [Condition?]
       /      \
   True       False
   /             \
[Repeat]        (Exit)
   |
  -----
"""
print("Example of Iteration Control Structure")
for i in range(5):
    print(i)
print("Loop ended")

################################################################
