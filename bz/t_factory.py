class Carfactory:
    def createCar(self,brand):
        if brand=="bc":
            return Benz()
        elif brand=="bm":
            return BMW()

class Benz:
    pass
class BMW:
    pass
class BYD:
    pass
factory=Carfactory()
