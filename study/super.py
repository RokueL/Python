
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable): # super는 다중상속의 경우 앞의 것을 한다
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()



