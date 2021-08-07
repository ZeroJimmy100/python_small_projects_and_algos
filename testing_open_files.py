# file = open("test_text_file.txt")
# print(file.readline())
# print(file.readline())
# print(file.read())
# file.close()

# with open("test_text_file.txt") as file:
#     print(file.readline())

# with open("test_text_file.txt") as file:
#     for line in file:
#         print(line.upper())

# with open("test_text_file.txt") as file:
#     for line in file:
#         print(line.strip().upper())

import os 
import datetime
import csv

# os.remove function remove an existing file within the directory 

# os.remove("test_text_file.txt")

# os.path.exists function checks if the file exist within the 
# current directory

print(os.path.exists("Users.py"))
print(os.path.exists("test_text_file.txt"))

# os.path.getsize function helps check how big the file is, in bytes

print(os.path.getsize("Users.py"))

# os.path.getmtime function help check when the file is last modify
# It will return a timestamp, Unix timestamp
print(os.path.getmtime("Users.py"))

# best way to convert the os.path.getmtime to standard timestamp
timestamp = os.path.getmtime("Users.py")
print(datetime.datetime.fromtimestamp(timestamp))

# os.path.abspath function gets the path of the file
print(os.path.abspath("Users.py"))

# os.getcwd function gets the current directory you are in
print(os.getcwd())

# os.mkdir function creates a new directory file
# os.mkdir("new_dir")

#os.chdir function change your current directory to the one you 
# want to go to

# os.chdir("hello_world")
# print(os.getcwd())

# os.rmdir function removes a directory and 
# it only works if the file exist 

# os.mkdir("newDir")
# os.rmdir("newDir")

# os.listdir help us see the files within a directory

print(os.listdir("hello_world"))

# to create make sure you know what path to go to, you can use 
# os.path.join function to see all full path within a directory
# and use a isdir function to check if it's a subfolder

# dir = "hello_world"
# for name in os.listdir(dir):
#     fullname = os.path.join(dir, name)
#     if os.path.isdir(fullname):
#         print("{} is a directory".format(fullname))
#     else:
#         print("{} is a file".format(fullname))

# def new_directory(directory, filename):
#     if os.path.isdir(directory) == False:
#         os.mkdir(directory)
    
#     os.chdir(directory)
#     with open(filename, "x") as file:
#         pass

#     return os.listdir()

# print(new_directory("PythonPrograms", "script.py"))

# hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
# with open('hosts.csv', 'w') as hosts_csv:
#     writer = csv.writer(hosts_csv)
#     writer.writerows(hosts)

# using dictionaries with csv files

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
{"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
{"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

keys = ["name", "username", "department"]

with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)