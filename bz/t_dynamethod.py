class Person:
    def work(self):
        print("work")
def play_game(self):
    print("play_game")
def work2(s):
    print("work2")
Person.work=work2
Person.play=play_game
p=Person()
p.play()
p.work()