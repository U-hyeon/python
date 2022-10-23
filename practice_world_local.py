gun = 10 # world

def checkpoint(soldiers): #경계근무
    # gun = 20 # local
    global gun # 전역공간에 있는 gun을 함수 내에서 사용하겠다
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers # local 변수이다!!
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # local 변수 gun을 반환하여 world값에 저장가능

print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 경계근무나감
# checkpoint_ret(gun,2) #2명이 경계근무나감
gun = checkpoint_ret(gun,2) #2명이 경계근무나감
print("남은 총 : {0}".format(gun))