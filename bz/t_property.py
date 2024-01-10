#测试@property
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    @property
    def print_sqlary(self):
        print("month,{0},yare,{1}".format(self.__salary,self.__salary*12))
        return self.__salary
    @print_sqlary.setter
    def print_sqlary(self,salary):
        if(0<salary<1000000):
            self.__salary=salary
        else:
            print("error")

emp1=Employee("lst",999)
print(emp1.print_sqlary)
emp1.print_sqlary=1000