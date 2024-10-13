# Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.
# Task 1: Directory Inspector:
# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.
# Code Example:
# import os
# def list_directory_contents(path):
# List and print all files and subdirectories in the given path
# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.

welcome_message = "Welcome to the Directory Inspector!"
print(welcome_message)

new_file = open("directory_inspector.txt", "w")
new_file.write(welcome_message)
new_file.close()








import os

def list_directory_contents(path):
    try:
        # List all files and subdirectories in the given path
        contents = os.listdir(path)
        print("Directory contents:")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied to access the directory.")
    except Exception as e:
        print("An error occurred:", e)
        
# Prompt the user for the directory path
path = input("Enter the directory path: ")
list_directory_contents(path)

     