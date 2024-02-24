# ------------------------------------------------- #
# Title: Demo06 - Working with lists and files
# Description: Write and Reading file data using a list of lists (two-dimensional table)
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# Data --------------------------------------------- #
FILE_NAME: str = 'MyData.txt'
student_row01: list = ["Vic", "Vu", 3.2]
student_row02: list = ["Sue", "Jones", 3.9]
student_table: list = [student_row01, student_row02]
file_data: str = ''
file = None

# Processing --------------------------------------- #


# Write to the file
file = open(FILE_NAME, "w")

for each in student_table:
    # Create a string representation for each student's data
    string_row = f"{each[0]},{each[1]},{each[2]}\n"

    # Write the data to the file
    file.write(string_row)

file.close()

# Read from the file
file = open(FILE_NAME, "r")
for each_row in file.readlines():
    # The the data comes from the file as a string
    # So, we transform the string data to a list
    student_data = each_row.split(',')
    # we will also remove the new-line and convert the GPA to a float data type
    student_data = [student_data[0], student_data[1], float(student_data[2].strip())]
    # Load it into our collection (list of lists)
    student_table.append(student_data)
file.close()



