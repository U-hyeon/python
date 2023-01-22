class Unit:
    def __init__(self, name, hp, speed): #생성자
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): #생성자
        Unit.__init__(self,name,hp, speed)
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}  파괴되었습니다.".format(self.name))

#드랍쉽 : 공중유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격 x

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): #다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # method overriding
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, location) # self 써야힘
        super().__init__(name, hp, 0) # ()사용, self 안씀
        self.location = location