# ------------------------------------------------- #
# Title: Demo02 - Using Parameters
# Description: Demonstrates how to use function parameters in your code
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script

# Notes:
#  * Add this starting data to the MyData.json file as needed.
# [{"FirstName": "Vic", "LastName": "Vu"}, {"FirstName": "Sue", "LastName": "Jones"}]
# ------------------------------------------------- #
import json
import io as _io

# Global Data --------------------------------------------- #
FILE_NAME: str = '../MyData.json'
# file = _io.TextIOWrapper
student_table: list = []

# Processing --------------------------------------- #
def read_data_from_file(file_name: str, student_data: list):
    # global FILE_NAME
    # global student_table

    try:
        file = open(file_name, "r")  # file is NO LONGER SHADOWING
        # student_table = json.load(file)
        # for item in student_table:

        student_data = json.load(file)
        for item in student_data:
            print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}")
    except FileNotFoundError as e:
        print("Text file must exist before running this script!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    except Exception as e:
        print("There was a non-specific error when reading the file!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    finally:
        if file.closed == False:
            file.close()
    # return student_data  # Without this student data will not be updated


def add_data_to_table(student_data: list):
    # global student_table

    try:
        # Check that the input does not include numbers
        student_first_name = input("Enter the student's first name: ")
        if not student_first_name.isalpha():
            raise ValueError("The first name should not contain numbers.")
        student_last_name = input("Enter the student's last name: ")
        if not student_last_name.isalpha():
            raise ValueError("The last name should not contain numbers.")

        student_data.append({"FirstName": student_first_name, "LastName": student_last_name})

    except ValueError as e:
        print(e)  # Prints the custom message
        print("-- Technical Error Message -- ")
        print(e.__doc__)
        print(e.__str__())
    except Exception as e:
        print("There was a non-specific error when adding data!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')

    return student_data  # Without this student data will not be updated

def write_data_to_file(file_name: str, student_data: list):
    # global FILE_NAME
    # global file
    # global student_table

    try:
        file = open(file_name, "w")
        json.dump(student_data, file)
    except FileNotFoundError as e:
        print("Text file must exist before running this script!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    except Exception as e:
        print("There was a non-specific error!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    finally:
        if file.closed == False:
            file.close()

    # We not need to return data in this function

#  End of function definitions

# Beginning of the main body of this script

# Read from the JSON file
student_table = read_data_from_file(file_name=FILE_NAME, student_data=student_table)
print(student_table)

# Add more data
student_table = add_data_to_table(student_data=student_table)

# Save data using json module
write_data_to_file(file_name=FILE_NAME, student_data=student_table)


