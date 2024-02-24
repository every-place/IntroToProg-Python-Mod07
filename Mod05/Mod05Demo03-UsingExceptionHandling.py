# ------------------------------------------------- #
# Title: Demo06 - Working with exception handling
# Description: Demonstrates how to use exception handling in your code
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script

# Notes:
#  * Add this starting data to the MyData.json file as needed.
# [{"FirstName": "Vic", "LastName": "Vu"}, {"FirstName": "Sue", "LastName": "Jones"}]
# ------------------------------------------------- #
import json
import io as _io

# Data --------------------------------------------- #
FILE_NAME: str = 'MyData.json'
file = _io.TextIOWrapper
student_table: list = []

# Processing --------------------------------------- #
# Read from the JSON file
try:
    file = open(FILE_NAME, "r")
    student_table = json.load(file)
    for item in student_table:
        print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}")
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Add more data
try:
    # Check that the input does not include numbers
    student_first_name = input("Enter the student's first name: ")
    if not student_first_name.isalpha():
        raise ValueError("The first name should not contain numbers.")

    student_last_name = input("Enter the student's last name: ")
    if not student_last_name.isalpha():
        raise ValueError("The last name should not contain numbers.")

    student_table.append({"FirstName": student_first_name, "LastName": student_last_name})
    
except ValueError as e:
    print(e)  # Prints the custom message
    print("-- Technical Error Message -- ")
    print(e.__doc__)
    print(e.__str__())
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')


# Save data using json module
try:
    file = open(FILE_NAME, "w")
    json.dump(student_table, file)
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()




