class AgeError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo=errorInfo
    def __str__(self):
        return str(self.errorInfo)+",age error,age should in 1-150"
if __name__=="__main__":
    age=int(input("please input age:"))
    if age<1 or age>150:
        raise AgeError(age)
    else:
        print("age is:",age)