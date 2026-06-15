import os 
directory_path = 'c'
# select directory
contents=os.listdir(directory_path)
# print file directory name 
for item in contents:
    print(item)