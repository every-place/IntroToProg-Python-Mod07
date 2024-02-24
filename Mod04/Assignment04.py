# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   ADean,2/5/2024,Created Script
#   ADean,2/5/2024,Discovered List does not write to file, only string
#   ADean,2/7/2024,Tested Menu options 1 and 2 for display
#   ADean,2/7/2024,Got clarity on what to write to Enrollments.csv
#   ADean,2/7/2024,Finished assignment
#
# ------------------------------------------------------------------------------------------ #

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
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
sample_student: list = ["John", "Doe", "Orientation"] # Sample data
student_table: list = [sample_student] # Holds sample data in 2D table
file_data: str = '' # # Holds combined string data separated by a comma.
file = None # Hold a reference to the starter information file
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: list = [] # Holds an individual student's registration information.
students: list  = [] # Holds all the student_data lists

# Put Starter Data in Enrollments.csv
file_obj = open(FILE_NAME, "w")

for each in student_table:
    # Create a string representation for each student's data
    string_row = f"{each[0]},{each[1]},{each[2]}\n"

    # Write the data to the file
    file_obj.write(string_row)

file_obj.close()

# Read from the file
file_obj = open(FILE_NAME, "r")
for row in file_obj.readlines():
    # The the data comes from the file as a string
    # So, we transform the string data to a list
    student_data = row.split(',')
    # we will also remove the new-line using .strip
    student_data = [student_data[0], student_data[1], (student_data[2].strip())]
    csv_data += f'{student_data[0]},{student_data[1]},{(student_data[2])}\n'
    # Load it into our collection (list of lists)
    students.append(student_data)
file_obj.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data, store in CSV and 2D table formats
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        csv_data += f'{student_first_name},{student_last_name},{course_name}\n'
        student_data = [student_first_name,student_last_name,course_name]
        students.append(student_data)
        continue

    # Present the current data, add student_data as a list to the table
    elif menu_choice == "2":
        print("\nThe current data is:")
        print(csv_data)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file_obj = open(FILE_NAME, "w")
        file_obj.write(str(csv_data))
        file_obj.close()
        for each in students:
            # Iterate through the csv_data for each student's data
            string_row = f"You have enrolled {each[0]} {each[1]} in {each[2]}"
            print(string_row)
        #print('Students:') # Test confirm 2D table is accurate
        #print(students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
