"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

"""

marks = {"Alice": 85, "Bob": 75, "Charlie": 60, "Daniel": 40, "Eve": 90, "Fred": 5}

def get_marks(name):
    if name in marks:
        return marks[name]
    else:
        return "Student not found"


name = input("Enter the student's name: ")
print(get_marks(name))