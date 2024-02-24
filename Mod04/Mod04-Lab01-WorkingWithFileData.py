# ------------------------------------------------------------------------------------------ #
# Title: Working with file data
# Desc: Shows how save data to a file
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
FILE_NAME: str = 'MyLabData.txt'

student_first_name: str = ''
student_last_name: str = ''
student_gpa: float = 0.0
message: str = ''
file_data: str = ''
file = None   # Not using type hint helps PyCharm, so we won't use it going forward

# Reset the file to be empty of data
file = open(FILE_NAME, 'w')
print(type(file))
file.close()


# Repeat the follow tasks
while True:

    # Input the data
    student_first_name = input("What is the student's first name? ")
    student_last_name = input("What is the student's last name? ")
    student_gpa = float(input("What is the student's GPA? "))


    # Process the data to create custom messages
    if student_gpa >= 4.0:
        message = "{} {} earned an A with a {:.2f} GPA"
    elif student_gpa >= 3.0:
        message = "{} {} earned a B with a {:.2f} GPA"
    elif student_gpa >= 2.0:
        message = "{} {} earned a C with a {:.2f} GPA"
    elif student_gpa >= 1.0:
        message = "{} {} earned a D with a {:.2f} GPA"
    else:
        message = "{} {}'s {:.2f} GPA was not a passing grade"

    # Output the data
    print(message.format(student_first_name, student_last_name, student_gpa))

    # Ask if the user wants to save this data to a file
    strChoice = input('Save data to the file ("y/n"): ')
    if strChoice == 'y':
        file = open(FILE_NAME, 'a')
        file.write(f'{student_first_name},{student_last_name},{student_gpa}\n')
        file.close()

    # Ask if the user wants to add more data
    strChoice = input('Add more data ("y/n"): ')
    if strChoice == 'y':
        continue  # to the start of the while loop
    else:
        break  # out of the while loop
