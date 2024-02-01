import os
import os.path
path=os.getcwd()
file_list=[filenames for filenames in os.listdir(path) if filenames.endswith(".py")]
for filename in file_list:
    print(filename)