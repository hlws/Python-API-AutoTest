s={"name":"shaoteng","age":28,"job":"dev"}
name,age,job=s#默认对键进行操作
print(name)
name,age,job=s.items()#对键值对操作
print(age)
name,age,job=s.values()
print(job)
