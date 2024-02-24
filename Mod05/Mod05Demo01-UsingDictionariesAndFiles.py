# ------------------------------------------------- #
# Title: Demo01 - Working with lists and files
# Description: Write and Reading file data using a list of dictionary rows (two-dimensional table)
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# Data --------------------------------------------- #
FILE_NAME: str = 'MyData.csv'
# student_row01: list = ["Vic", "Vu"]
# student_row02: list = ["Sue", "Jones"]
student_row1: dict = {"FirstName": "Vic", "LastName": "Vu"}
student_row2: dict = {"FirstName": "Sue", "LastName": "Jones"}
student_table: list = [student_row1, student_row2]

file_data: str = ''
file = None

# Processing --------------------------------------- #

# Show the current data
print("\n--- Displaying data ---")
for row in student_table:
    print(f'{row["FirstName"]},{row["LastName"]}')
print("=" * 30)


# Add a new dictionary row
student_first_name = input("Enter the student's first name: ")
student_last_name = input("Enter the student's last name: ")
student_data = {"FirstName": student_first_name, "LastName": student_last_name}
student_table.append(student_data)

# Show the current data
print("\n--- Displaying data ---")
for row in student_table:
    print(f'{row["FirstName"]},{row["LastName"]}')
print("=" * 30)

first_name = input("Enter the first name to remove: ")

# Removed data from the table
for row in student_table:
    if first_name.lower() == row["FirstName"].lower():
        student_table.remove(row)

# Show the current data
print("\n--- Displaying data ---")
for row in student_table:
    print(f'{row["FirstName"]},{row["LastName"]}')
print("=" * 30)

# Write to the file
file = open(FILE_NAME, "w")
for row in student_table:
    # Create a string representation for row student's data
    # string_row = f"{row[0]},{row[1]}\n"
    string_row = f'{row["FirstName"]},{row["LastName"]}\n'
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
    # student_data = [student_data[0], student_data[1], float(student_data[2].strip())]
    student_data = {"FirstName": student_data[0], "LastName": student_data[1].strip()}
    # Load it into our collection (list of lists)
    student_table.append(student_data)
file.close()
