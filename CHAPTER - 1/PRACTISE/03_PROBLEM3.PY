import os

# specify the directory path you want to list
directory_path = '/'

# list the contents of the directory
contents = os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)