class MobilPhone:
    def __init__(self,cpu,screen):
        self.cpu=cpu
        self.screen=screen
class CPU:
    def calculate(self):
        print("cal")
class Screen:
    def show(self):
        print("show")
c=CPU()
s=Screen()
m=MobilPhone(c,s)
m.cpu.calculate()
m.screen.show()