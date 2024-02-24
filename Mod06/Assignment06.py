# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions, classes, and Separation of Concern
# with structured error handling
# Change Log: (Who, When, What)
#   ADean,18FEB24,Created Script
#   ADean,18FEB24,Set Layout for Architecture
#   ADean,19FEB24,Placeholders for functions
#   ADean,20FEB24,Added code to function placeholders, tested
#   ADean,21FEB24,Created endless loop with print(menu) - resolved
#   ADean,21FEB24,Finished assignment
#
#
# ------------------------------------------------------------------------------------------ #
import json

#-- Data --#
# Declare variables, constants, and files
# Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = '../Enrollments.json'

# Variables
menu_choice: str = ''
students: list = []
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.

# Classes
class FileProcessor:
    '''
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    ADean,19FEB24,Created Class with fx placeholders
    ADean,20FEB24,Wrote several functions
    ADean,21FEB24,Finished functions
    '''
    @staticmethod
    def prep_json_file(file_name: str):
        ''' This function prepares the Enrollments.json file

        ChangeLog: (Who, When, What)
        ADean,20FEB24,Wrote function
        ADean,21FEB24, Finished and tested

        :param file_name: Uses the fiel neame constant
        :return: Enrollments.json file
        '''
        try:
            reg_list: dict[str,str,str] = [{"FirstName": "Vic", "LastName": "Vu", "CourseName": "Python 100"}, \
                                           {"FirstName": "Sue", "LastName": "Jones", "CourseName": "Python 200"}]
            file = open(file_name,'w')
            json.dump(reg_list,file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is in valid JSON format", e)
        finally:
             if file.closed == False:
                 file.close()

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        ''' This function reads data from the student_data file

        ChangeLog: (Who, When, What)
        ADean,19FEB24,Created function placeholder
        ADean,20FEB24,Wrote function
        ADean,21FEB24, Finished and tested

        :return: student_data with all registrations
        '''
        try:
            file = open(file_name, 'r')
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages('Text file must exist before running this script!', e)
        except Exception as e:
            IO.output_error_messages('There was a non-specific error!', e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        ''' This function writes the students data to the Enrollments.json file

        ChangeLog: (Who, When, What)
        ADean,19FEB24,Created Class with fx placeholders
        ADean,21FEB24, Finished and tested

        :return: Saves current enrollment data to Enrollments.json
        '''
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        print(f"Enrollments.json contains:\n{students}")


class IO:
    '''
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    ADean,19FEB24,Created Class with fx placeholders
    ADean,21FEB24, Finished and tested


    '''

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        ''' This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        ADean,19FEB24,Created function placeholder
        ADean,20FEB24,Wrote function
        ADean,21FEB24, Finished and tested

        :param message: 
        :param error: 

        :return: None
        '''
        print(message, end='\n\n')
        if error is not None:
            print('-- Technical Error Message --')
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        ''' This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        ADean,19FEB24,Created function placeholder
        ADean,20FEB24,Wrote function
        ADean,21FEB24,Finished and tested

        :param menu: the constant text menu
        :return: Displays menu
        '''
        print()
        print(menu)
        print()
    @staticmethod
    def output_student_courses(students: list):
        ''' Displays current student enrollment data

        ChangeLog: (Who, When, What)
        ADean,19FEB24,Created function placeholder
        ADean,21FEB24,Finished and tested
        
        :param students: students
        :return: Formatted lines of student enrollment
        '''
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        '''
        Collects student registration data and adds to student_data

        ChangeLog: (Who, When, What)
        ADean,19FEB24,Created function placeholder
        ADean,21FEB24,Finished and tested

        :param student_data: Collection of all student registration data
        :return: Individual student data
        '''
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)

        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        ADean,19FEB24,Created function placeholder
        ADean,20FEB24,Wrote function
        ADean,21FEB24,Finished and tested

        :return: string with the user\'s choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ") # This will not work with an integer!
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")

        except Exception as e:
            IO.output_error_messages(e.__str__()) # Not passing e to avoid technical message

        return choice

# -- Prep Enrollments.json  file with data --
reg_file = FileProcessor.prep_json_file(file_name=FILE_NAME)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,student_data=students)
# -- Display menu --
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()
# -- Get user menu input
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(students)
# -- Display student enrollments --
    elif menu_choice == "2": # Get new data (and display the change)
        IO.output_student_courses(students=students)
        continue
# -- Store registration data
    elif menu_choice == "3": # This writes the students temp file to the Enrollments.json file and savers it
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
# -- End program
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")


