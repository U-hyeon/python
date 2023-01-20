class Unit:
    def __init__(self, name, hp, damage): #생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중유닛, 비행기, 클로킹(보이지않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내것으로 빼앗음
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True # wraith2 라는 [객체]에 멤버변수를 추가

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# [클래스]가 아니라 wraith2라는 [객체]에 변수를 추가하였기 때문에
# wraith1 이라는 객체에는 clocking이라는 변수가 존재하지 않는다
# if wraith1.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))