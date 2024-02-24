# ------------------------------------------------------------------------------------------ #
# Title: WorkingWithListsAndFiles
# Desc: Shows how work with lists and files when using a table of data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
FILE_NAME: str = 'MyLabData.txt'

# Define the program's data
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''

student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
student_gpa: float = 0.0  # Holds the GPA of a student entered by the user.
message: str = ''  # Holds a custom message string
menu_choice: str = ''   # Hold the choice made by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
file_data: str = '' # Holds combined string data separated by a comma.
file = None  # Not using type hint helps PyCharm, so we won't use it going forward

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
file = open(FILE_NAME, "r")
for row in file.readlines():
    # Transform the data from the file
    student_data = row.split(',')
    student_data = [student_data[0], student_data[1], float(student_data[2].strip())]
    # Load it into our collection (list of lists)
    students.append(student_data)
file.close()

# Repeat the follow tasks
while True:

    print (MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer.

    if menu_choice == "1":
        # display a the data
        print("-"*50)
        for student in students:
            if student[2] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student[2] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student[2] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student[2] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student[0], student[1], student[2]))
        print("-"*50)
        continue
    elif menu_choice == "2":
        # Input the data
        student_first_name = input("What is the student's first name? ")
        student_last_name = input("What is the student's last name? ")
        student_gpa = float(input("What is the student's GPA? "))
        student_data = [student_first_name, student_last_name, student_gpa]
        students.append(student_data)
        continue

    elif menu_choice == "3":
        #  Save the data to the file
        file = open(FILE_NAME, "w")
        for student in students:
            file.write(f"{student[0]},{student[1]},{student[2]}\n")
        file.close()
        print("Data Saved!")
        continue

    elif menu_choice == "4":
        # Exit the program
        break  # out of the while loop

