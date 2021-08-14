# import re
# def show_time_of_pid(line):
#   pattern = r"(([A-Z].{14}).*(\[([0-9].*)\]))"
#   result = re.search(pattern, line)
#   return result[2] + "pid:" + result[4]

# print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

# print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

# print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

# print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

# print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

# print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

# print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

#!/usr/bin/env python3

import sys
import os
import re

def error_search(log_file):

# The input() function takes the input from the user and then evaluates the expression. 
# This means Python automatically identifies whether the user entered a string, a number, 
# or a list. If the input provided isn't correct then Python will raise either a syntax 
# error or exception. The program flow will stop until the user has given an input.

# Later in the script, we'll iterate over this user input and the log file to produce results. Following 
# the input function, now initialize the list returned_errors. This will enlist all the ERROR logs as specified 
# by the end-user through the input function.

  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r', encoding = 'UTF-8') as file:
    # For this, we'll create a list to store all the patterns (user input) that will be searched. 
    # This list is named error_patterns and, initially it has a pattern "error" to filter out 
    # all the ERROR logs only. You can change this to view other types of logs such as INFO and WARN. 
    # You can also empty initialize the list to fetch all types of logs, irrespective of their type.
    for log in file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))

        # use the search() method (present in re module) to check whether the file has the user defined pattern 
        # and, if it is available, append them to the list returned_errors.
        if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
          returned_errors.append(log)

    # close the file and return the results stored in the list returned_errors.
    file.close()
  return returned_errors

def file_output(returned_errors):
#   Using Python file handling methods, write returned_errors into the errors_found.log file by opening the file 
#   in writing mode. For defining the output file, use the method os.path.expanduser ('~'), 
#   which returns the home directory of your system instance. Then, 
#   concatenate this path (to the home directory) to the file errors_found.log in /data directory.
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:

    # write all the logs to the output file by iterating over returned_errors.
    for error in returned_errors:
      file.write(error)
    file.close()

# The variable log_file takes in the path to the log file passed as a parameter. In our case, 
# the file is fishy.log. Call the first function i.e., error_search() and pass the variable log_file 
# to the function. This function will search and return a list of errors that would be stored in the 
# variable returned_errors. Call the second function file_output and pass the variable returned_errors 
# as a parameter.

# sys.exit(0) is used to exit from Python, the optional argument passed can be an integer giving the exit 
# status (defaulting to zero), or another type of object. If it is an integer, zero is considered 
# "successful termination" and any nonzero value is considered an "abnormal termination" by shells.
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)