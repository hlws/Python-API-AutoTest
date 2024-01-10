class Student:
    company="clic"
    @classmethod
    def printCompany(cls):
        print(cls.company)
    @staticmethod
    def add(a,b):
        print(a+b)
Student.printCompany()
Student.add(10,20)