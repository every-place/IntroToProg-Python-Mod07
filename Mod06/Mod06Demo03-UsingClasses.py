# ------------------------------------------------- #
# Title: Demo03 - Using Classes
# Description: Demonstrates how to use classes with functions and simple data
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script

# Notes: You will learn about complex data classes in module 07

# ------------------------------------------------- #

class Results:
    """
    A collection of variables to hold arithmetic results Data

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    sum: float = 0.0
    difference: float = 0.0


class Calculator:
    """
    A collection of functions that perform arithmetic Processing

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def add(a: float, b: float):
        """ This function adds to values and returns a sum

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param a: float data used as the first number
        :param b: float data used as the second number
        :return: float data with the sum of the first and second numbers
        """

        return a + b

    @staticmethod
    def subtract(a: float, b: float):
        """ This function adds to values and returns a sum

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param a: float data used as the first number
        :param b: float data used as the second number
        :return: float data with the difference between the first and second numbers
        """

        return a - b


# Creating an instance of the Calculator class and the Results class
# calculator = Calculator()  # an object is not needed with static functions (methods)
results1 = Results()
results2 = Results()

# Using the functions and classes

print("Get first results")
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))
print()

# results1.sum = calculator.add(value1,value2)
# results1.difference = calculator.subtract(value1,value2)

results1.sum = Calculator.add(value1,value2)
results1.difference = Calculator.subtract(value1,value2)


print("Get second results")
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))
print()

results2.sum = Calculator.add(value1,value2)
results2.difference = Calculator.subtract(value1,value2)

print("Here are the two results")
print("First results: ", "Sum", results1.sum, "and Diff", results1.difference)
print("Second results: ", "Sum", results2.sum, "and Diff", results2.difference)

