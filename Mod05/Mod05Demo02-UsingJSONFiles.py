# ------------------------------------------------- #
# Title: Demo02 - Working with json files
# Description: Write and Reading file data using json
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
import json

# Data --------------------------------------------- #
student_row1: dict = {"FirstName": "Vic", "LastName": "Vu"}
student_row2: dict = {"FirstName": "Sue", "LastName": "Jones"}
student_table: list = [student_row1, student_row2]

file_data: str = ''
file = None

# Processing --------------------------------------- #
# Write to the  file

# CSV
file = open("MyData.csv", "w")
for each in student_table:
    string_row = f'{each["FirstName"]},{each["LastName"]}\n'
    file.write(string_row)
file.close()


# JSON automatically with json module
file = open("MyData.json", "w")
json.dump(student_table, file)
file.close()


# Note the function dump[s] convert the list of dictionary rows into a string.
json_data = json.dumps(student_table)
print(json_data, type(json_data))
print(student_table, type(student_table))


# Read from the CSV file
file = open("MyData.csv", "r")
for each_row in file.readlines():
    student_data = each_row.split(',')
    student_data = {"FirstName": student_data[0], "LastName": student_data[1].strip()}
    # Load it into our collection (list of lists)
    student_table.append(student_data)
file.close()


# Read from the JSON file
file = open("MyData.json", "r")
student_table = json.load(file)
for item in student_table:
    print(f"ID: {item['FirstName']}, Name: {item['LastName']}")
file.close()



