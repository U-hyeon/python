# import travel.thailand
# #import travel.thailand.ThailandPackage #함수 직접 import불가
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

#from random import *
from travel_temp import * # 패키지 내부 __init__에서 공개범위 설정해줘야한다
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage() 
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))