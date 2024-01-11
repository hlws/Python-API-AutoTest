class Carfactory:
    def createCar(self,brand):
        if brand=="bc":
            return Benz()
        elif brand=="bm":
            return BMW()
        elif brand=="BYD":
            return BYD()
        else:
            print("error")

class Benz:
    pass
class BMW:
    pass
class BYD:
    pass
factory=Carfactory()
c1=factory.createCar("BYD")
c2=factory.createCar("bm")
print(c1)
print(c2)