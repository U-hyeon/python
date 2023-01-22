class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): # 다중상속
    def __init__(self):
        # super().__init__() # self 사용시 : 다중상속 중 첫 상속만 생성자가 실행된다
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()