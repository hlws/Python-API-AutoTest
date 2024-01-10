class Animal:
    def shout(self):
        print("动物叫")
class Dog(Animal):
    def shout(self):
        print("狗叫")
class Cat(Animal):
    def shout(self):
        print("猫叫")
def animalShout(a):
    a.shout()
animalShout(Dog())
animalShout(Cat())
