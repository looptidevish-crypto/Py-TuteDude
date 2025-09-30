"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""

def open_file():
    file = open('sample.txt', 'r')
    file_content = file.read()
    print("Reading file content:")
    for i, line in enumerate(file_content.splitlines(), 1):
        print(f"Line {i}: ",line)
    file.close()

open_file()