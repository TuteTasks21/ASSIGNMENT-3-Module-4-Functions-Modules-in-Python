#Task 2: Using the Math Module for Calculations

import math
number = float(input("Enter a number: "))
if number >= 0:
    square_root = math.sqrt(number)
    try:
        natural_log = math.log(number) if number > 0 else float('-inf')
    except ValueError:
        natural_log = "Undefined"
else:
    square_root = "Undefined (cannot take square root of a negative number)"
    natural_log = "Undefined (logarithm is undefined for non-positive numbers)"

sine = math.sin(number)

print(f"Square root: {square_root}")
print(f"Logarithm : {natural_log}")
print(f"Sine : {sine}")
