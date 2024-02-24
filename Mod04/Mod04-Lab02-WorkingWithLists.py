# ------------------------------------------------------------------------------------------ #
# Title: Working with collections
# Desc: Shows how work with lists to represent a table of data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
MENU: str = '''
---- Student GPAs ----
  Select from the following menu:  
    1. Enter new student data
    2. Show current student data  
    3. Exit the program
----------------------------------------- 
'''
student_first_name: str = ''
student_last_name: str = ''
student_gpa: float = 0.0
message: str = ''
menu_choice: str = ''
student_data: list = []  # one row of student data
students: list = []  # a table of student data

# Repeat the follow tasks
while True:

    print (MENU)
    menu_choice = input("Enter your menu choice number: ")

    if menu_choice == "1":
        # Input the data
        student_first_name = input("What is the student's first name? ")
        student_last_name = input("What is the student's last name? ")
        student_gpa = float(input("What is the student's GPA? "))
        student_data = [student_first_name, student_last_name, student_gpa]
        students.append(student_data)  # No brackets
        continue
    elif menu_choice == "2":
        for student in students:
            # Process the data to create and display a custom messages
            if student[2] >= 4.0:
                message = "{} {} earned an A with a {:.2f} GPA"
            elif student[2] >= 3.0:
                message = "{} {} earned a B with a {:.2f} GPA"
            elif student[2] >= 2.0:
                message = "{} {} earned a C with a {:.2f} GPA"
            elif student[2] >= 1.0:
                message = "{} {} earned a D with a {:.2f} GPA"
            else:
                message = "{} {}'s {:.2f} GPA was not a passing grade"
            print(message.format(student[0], student[1], student[2]))
        continue
    elif menu_choice == "3":
        break  # out of the while loop
