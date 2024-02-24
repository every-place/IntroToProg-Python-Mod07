# ------------------------------------------------------------------------------------------ #
# Title: Working with multiple conditions
# Desc: Shows how conditional logic statements work
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #


# Define the program's data
grade: float = 0
total_grade_points : float = 0
grade_point_average: float = 0
counter: int = 0
menu:str = ''
choice:str = ''
list_of_grade_points: str = ''

while True:
    menu = """ 
    Select and enter a number based on the following options:
    1. Enter a new grade
    2. Display the currently entered grades
    3. Display the GPA
    4. Display the equivalent letter grade 
    5. Exit the program    
    """
    print(menu)
    choice = input("Enter a menu option (1-5): ")

    if choice == "1":
        grade = input("Enter the grade number (ex. 3.5): ")
        list_of_grade_points += (grade + ',')  # Add the grade to our list

    elif choice == "2":
        print(list_of_grade_points)

    elif choice == "3":
        for grade in list_of_grade_points.split(','):  # Using split to separate the values
            if grade != '':  # Needed to handle the last comma in the string (ex. 4.0,2.5,)
                total_grade_points += float(grade)
                counter += 1
        grade_point_average = total_grade_points / counter
        print("The current GPA is :", grade_point_average)

    elif choice == "4":
        if grade_point_average >= 4.0:
            message = " A GPA of {:.2f} equals an A"
        elif grade_point_average >= 3.0:
            message = "A GPA of {:.2f} equals a B"
        elif grade_point_average >= 2.0:
            message = "A GPA of {:.2f} equals a C"
        elif grade_point_average >= 1.0:
            message = "A GPA of {:.2f} equals a D"
        else:
            message = "A GPA of {:.2f} is not a passing grade"
        print(message.format(grade_point_average))

    elif choice == "5":
        print("Ending program")
        exit()

