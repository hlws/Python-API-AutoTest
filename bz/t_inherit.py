class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_age(self):
        print(self.name,"年龄是：",self.age)
    def say_name(self):
        print("我是",self.name)
class Student(Person):
    def __init__(self,age,name,score):
        Person.__init__(self,age,name)
        self.score=score
        # self.name=name
        # self.age=age
    def say_score(self):
        print(self.name,"的分数是",self.score)
    def say_name(self):
        print("student:",self.name)
s1=Student("lst",15,99)
s1.say_score()
s1.say_name()
s1.say_age()
print(Student.mro())
print(s1.__str__())

