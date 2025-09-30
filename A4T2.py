"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""


# Step 1: Take user input and write it to a file
first_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(first_input + "\n")

print("Data successfully written to output.txt.")

additional_input = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

print("Data successfully appended.")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)
