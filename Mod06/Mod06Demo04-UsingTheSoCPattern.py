# ------------------------------------------------- #
# Title: Demo04 - Using classes and the SoC pattern
# Description: Demonstrates how to use classes and the SoC pattern in your code
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# RRoot,1.2.2030,Added a menu of options

# Notes:
#  * Add this starting data to the MyData.json file as needed.
# [{"FirstName": "Vic", "LastName": "Vu"}, {"FirstName": "Sue", "LastName": "Jones"}]
# ------------------------------------------------- #
import json

# Global Data --------------------------------------------- #
FILE_NAME: str = '../MyData.json'
MENU = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current data.
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
    '''

student_table: list = []
menu_choice = ''


# Processing --------------------------------------- #
class ProcessFileData:
    """
    A collection of processing layer functions that work with json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file into a list of dictionary rows

        Notes:
        - Data sent to the student_data parameter will be overwritten.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.3.2030,Removed presentation layer code

        :param file_name: string with the name of the file we are reading
        :param student_data: list of dictionary rows we are adding data to
        :return: list of dictionary rows filled with data
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            # Moving this code the I/O class
            # for item in student_data:
            #     print(f"ID: {item['FirstName']}, Name: {item['LastName']}")
        except FileNotFoundError as e:
            # We will send to error messages to a function in IO
            IO.output_error_messages("Text file must exist before running this script!", e)
            # print("Text file must exist before running this script!\n")
            # print("-- Technical Error Message -- ")
            # print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when reading the file!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.3.2030,Removed presentation layer code

        :param file_name: string with the name of the file we are writing to
        :param student_data: list of dictionary rows we containing our data
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!",e)
        finally:
            if file.closed == False:
                file.close()


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

          Note: We can now customize our error messages in one place and affect all the error handling!

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        RRoot,1.4.2030,Added code to toggle technical message off if no exception object is passed

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_current_data(student_data: list):
        """ This function displays the current data to the user

        :return: None
        """
        print('='*40)
        for item in student_data:
            print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}")
        print('='*40, end='\n\n')  # Adding extra space to make it look nicer.

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu of option to the user

        :return: None
        """
        print(menu,end='\n\n')  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("You must choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def input_data_to_table(student_data: list):
        """ This function gets data from the user and adds it to a list of dictionary rows

        :param student_data: list of dictionary rows containing our current data
        :return: list of dictionary rows filled with a new row of data
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            student_data.append({"FirstName": student_first_name, "LastName": student_last_name})

        except ValueError as e:
            IO.output_error_messages("Only use names without numbers", e)  # Prints the custom message
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when adding data!", e)

        return student_data

#  End of class definitions


# Beginning of the main body of this script

student_table = ProcessFileData.read_data_from_file(
                    file_name=FILE_NAME, student_data=student_table)


# Repeat the follow tasks
while True:
    IO.output_menu()
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.output_current_data(student_data=student_table)
        continue

    if menu_choice == "2":
        student_table = IO.input_data_to_table(student_data=student_table)
        print("\n Here is the updated data")
        IO.output_current_data(student_data=student_table)
        continue

    elif menu_choice == "3":
        ProcessFileData.write_data_to_file(file_name=FILE_NAME, student_data=student_table)
        continue

    elif menu_choice == "4":
        break  # out of the while loop



