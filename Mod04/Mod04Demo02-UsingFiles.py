# ------------------------------------------------- #
# Title: Demo02 - Using files
# Description: This script demonstrates Reading from a file with read()
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# Data --------------------------------------------- #
FILENAME: str = 'MyData.txt'
file_data: str = ''
file = None

# Processing --------------------------------------- #
file = open(FILENAME, "w")
file.write('Vic' + '\t' + 'Vu' + '\n')
file.close()
# Pause and check the file!

file = open(FILENAME, "w")
file.write('Bob' + ',' + 'Baker' + '\n')
file.close()
# Pause and check the file!

file = open(FILENAME, "a")
file.write('Sue' + ',' + 'Salias' + '\n')
file.close()
# Pause and check the file!

file = open(FILENAME, "r")
file_data = file.read()  # read all the data in the file at once
file.close()
print('Here is the data from the file:')
print(file_data)
print('^ Note the extra blank line was read from the file too! ^')

file = open(FILENAME, "r")
file_data = file.readline()  # read one row of data the data in the file at once
file.close()
print('Here one row of the data from the file:')
print(file_data)




