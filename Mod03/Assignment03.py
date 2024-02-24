# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using conditional statements in a while loop, appending
#   data to csv file, and reading a csv file.
# Change Log: (Who, When, What)
#   ADean,31JAN24,Created Script
#   ADean,31JAN24,Modified csv_data string format. Revised csv file creation.
#
# ------------------------------------------------------------------------------------------ #
# Define the Data Constants
MENU: str =  '''
---- Course Registration Program ----
Select from the following menu:
  1. Register a Student for a Course
  2. Show current data
  3. Save data to a file
  4. Exit the program
-----------------------------------------
'''
FILE_NAME: str = '../Mod04/Enrollments.csv'

# Define the Data Variables
student_first_name: str
student_last_name: str
course_name: str
csv_data: str = '' # Assigned Value '', so appending data would work
file_obj: None
menu_choice: str

# Input user data
while True:
    print(MENU)
    menu_choice = input('Please enter your choice: ')
    # Conditional statements for menu choices
    if menu_choice == '1':
        student_first_name = input('Enter the student\'s First Name: ')
        student_last_name = input('Enter the student\'s Last Name: ')
        course_name = input('Enter the student\'s Course Name: ')
        csv_data += f'{student_first_name},{student_last_name},{course_name}\n'
        continue
    # Present the current data
    elif menu_choice == '2':
        print('The current data is:\n' + csv_data)
        continue
    # Save the data to a file
    elif menu_choice == '3':
        file_obj = open(FILE_NAME, 'a')
        file_obj.write(csv_data)
        file_obj.close()
        print('You have registered:\n'+ csv_data)
        continue
    # Stop the loop
    elif menu_choice == '4':
        print('Thank you for registering.\nEnd of Line.')
        exit()
    else:
        print("Let's try again...")