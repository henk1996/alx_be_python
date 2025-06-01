# Instructions:

# Prompt User for Pattern Size:

# Ask the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square): Enter the size of the pattern:.
# Draw the Pattern:

# First, use a while loop to iterate through each row of the pattern.
# Inside the while loop, use a for loop to print asterisks (*) side by side without advancing to a new line (you can use print("*", end="") for this).
# After completing each row, print a newline character to move to the next row.
# Continue until the pattern forms a square of the inputted size.
# Example Interaction:

# If the user inputs 4, the output should be:

# Enter the size of the pattern: 4
# ****
# ****
# ****
# ****

user = int(input("Enter the size of the pattern: "))

i = 1

while i <= user:
    for j in range(user):
        print("*", end="")
    print()
    i = i + 1