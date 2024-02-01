import os
path=os.getcwd()
file_list=os.walk(path,topdown=False)
for  root,dir,file in file_list:
    for name in file:
        print(os.path.join(root,name))
    for name in dir:
        print("dir_t")
        print(os.path.join(root,name))
print("#######")
print(root)
print(path)