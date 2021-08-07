#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
        # DictReader creates an object that operates like a regular reader 
        # (an object that iterates over lines in the given CSV file), 
        # but also maps the information it reads into a dictionary 
        # where keys are given by the optional fieldnames parameter. 
        # If we omit the fieldnames parameter, the values in the first row 
        # of the CSV file will be used as the keys. So, in this case, 
        # the first line of the CSV file has the keys and so there's 
        # no need to pass fieldnames as a parameter.

        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        
        # The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
        employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
        
        employee_list = []

        # Append the dictionaries to an empty initialised list employee_list
        for data in employee_file:
                employee_list.append(data)
        return employee_list

# will return this dicationary in the format department:amount, 
# where amount is the number of employees in that particular department.
def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data

# This function writes a dictionary of department: amount to a file
# The report should have the format:
# <department1>: <amount1>
#<department2>: <amount2>
def write_report(dictionary, report_file):
    # use the open() function to open a file and return a corresponding 
    # file object. This function requires file path and file mode to be 
    # passed as parameters. The file mode is 'r' (reading) by default, 
    # so you should now explicitly pass 'w+' mode (open for reading 
    # and writing, overwriting a file) as a parameter.
        with open(report_file, 'w+') as f:
                for k in sorted(dictionary):
                        f.write(str(k)+':'+str(dictionary[k])+'\n')
                f.close()


# file_location should be replace with a csv file for this to work
# the original lesson has /home/<username>/data/employees.csv within 
# the file_location
employee_list = read_employees('<file_location>')
# print(employee_list)

dictionary = process_data(employee_list)
# print(dictionary)

# report_file should be replace with a text file
# This script does not generate any output, but it creates a new file 
# named report.txt within the data directory. This report.txt 
# file should now have the count of people in each department.
# original lesson has /home/<username>/data/report.txt that replace the
# report_file
write_report(dictionary, '<report_file>')