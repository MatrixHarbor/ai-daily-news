# 3！= 3*2*1 = 6
from math import factorial

# Ask the user for a number n.
# Make sure number n is a positive integer
# Need to set a factorial = 1
# For loop that allows us to iterate from 1 to n  # For loop when I have a definitive number of time to compute  # while loop is used when I have infinitive number, I don't
# Within the loop, I will multiply my total_number by the current number n
# Print the factorial of n
# I want to

n = input("Enter a number: ")
n = float(n)

factorial = 1

for number in range(1, n+1): #
    factorial = factorial*number
print(f"factorial of {n} is {factorial}")

