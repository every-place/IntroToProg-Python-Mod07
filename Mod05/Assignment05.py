# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   ADean,2/8/2024,Created Script
#   ADean,2/10/2024,Verified all variables were present
#   ADean,2/12/2024,Tested Data Entry
#   ADean,2/14/2024,Tested JSON manipulation, Error Handling
#
# ------------------------------------------------------------------------------------------ #
import json
from io import TextIOWrapper

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Prep the Enrollments.json file with data so as not to get a read error
row1 = {"FirstName": "Fred", "LastName": "Flintstone", "CourseName": "Geology 101"}
row2 = {"FirstName": "Barney", "LastName": "Rubble", "CourseName": "History 101"}
table = [row1, row2]

# Write the contents to a file for each row in the table
file = open(FILE_NAME, 'w')

file.write('[\n')
file.write(f'{{"FirstName": "{row1["FirstName"]}", "LastName": "{row1["LastName"]}", "CourseName": "{row1["CourseName"]}"}},\n')
file.write(f'{{"FirstName": "{row2["FirstName"]}", "LastName": "{row2["LastName"]}", "CourseName": "{row2["CourseName"]}"}}\n')
file.write(']')

file.close()


# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''  # Holds all the registrations in json format.
student_data: dict = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
# Error handling when the file is read into the list of dictionary rows
try:
    file = open(FILE_NAME, "r")
    # On start, read contents of "Enrollments.json" into 2D list table(list of dictionary rows)
except FileNotFoundError as e:
    print("Text file must exist before running this script!]\n")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')


json_data = json.load(file)

#print(f'JSON Data: {json_data}')

for row in json_data:
    # All data in the list is displayed when menu choice 2 is used.
    student_data = f'{row["FirstName"]} {row["LastName"]} is enrolled in {row["CourseName"]}'
    students += f'{student_data}\n'
    print(student_data)


file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        # Error handing when the user enters a first name
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')

        try:
            # Error handing when the user enters a last name
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')

        course_name = input("Please enter the name of the course: ")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Present a string by formatting the collected data using the print() function
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        print("-" * 50)
        # Data collected for menu choice 1 is added to a 2D list table
        json_data.append({"FirstName":student_first_name, "LastName": student_last_name, "CourseName": course_name})
        #
        for row in json_data:
            # All data in the list is displayed when menu choice 2 is used.
            student_data = f'{row["FirstName"]} {row["LastName"]} is enrolled in {row["CourseName"]}'
            students += f'{student_data}\n'
            print(student_data)
        #print(f"JSON Data: {json_data}")
        continue

    # Save the data to a file
    elif menu_choice == "3":
        # Error handling when the dictionary rows are written to the file
        try:
            # Open a file named Enrollments.json with the open() function
            file = open(FILE_NAME, "w")
            json.dump(json_data, file)
            print("The following data was saved to file!")
            print(json_data)
            file.close()
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")