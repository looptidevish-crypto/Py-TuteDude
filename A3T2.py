"""
Task 2: Using the Math Module for Calculations

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

"""
import math
num = int(input("Enter a number: "))
def calculate(num):
    sq_root = math.sqrt(num)
    log_root = math.log(num)
    sin = math.sin(num)
    return sq_root, log_root, sin

sq_root, log_root, sine = calculate(num)
print(f"Square root: {sq_root}")
print(f"logarithm: {log_root}")
print(f"Sine : {sine}")