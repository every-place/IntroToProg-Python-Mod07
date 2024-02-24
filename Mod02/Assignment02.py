# ------------------------------------------------------------------------------------------ #
# Title: Assignment02
# Desc: This assignment demonstrates using constants, variables, formatted string concatenation,
#   math calculation, formatting float values in strings, and creating, reading, and writing
#   to CSV files.
#
# Change Log: (Who, When, What)
#   ADean,21JAN24,Created Script
#
# ------------------------------------------------------------------------------------------ #
# Set constants and variables
COURSE_NAME: str = 'Python 100'
COURSE_PRICE: str = 999.98
STATE_TAX: float = .09
TOTAL_PRICE: float = COURSE_PRICE + COURSE_PRICE * STATE_TAX
FILE_NAME: str  = '../Mod04/Enrollments.csv'

student_first_name: str = ''
student_last_name: str = ''
course_name: str = '' # not used
csv_data: str = ''
file_obj = None

# User Inputs
student_first_name = input("Enter student's first name: ")
student_last_name = input("Enter student's last name: ")

# Screen Output (Test)
message: str = '.'
message = f'{student_first_name},{student_last_name},\
{COURSE_NAME},{COURSE_PRICE},{TOTAL_PRICE:.2f}'
message += '\n'
print(message)

# CSV File Output
csv_file = open(FILE_NAME,'w',newline='') # I used the truncating parameter 'w' for
# this simple exercise and added the "newline" parameter based on some articles.
# Using the append 'a' parameter is useful for creating a log of entries rather than
# a single use scenario.

csv_file.write(message)
csv_file.close()


