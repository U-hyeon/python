# 당신의 학교에서는 파이썬 코딩 대회를 주회합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게됩니다.
# 추첨 프로그램을 작성하시오

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle과 sample을 활용

# 출력예제
# --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# --축하합니다--

# 활용예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))


# -- my code --
from random import *
# users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = range(1,21) # 1~21 '직전'까지!
print(type(users)) # type = range
users = list(users) #자료구조의 변경 -> list
print(type(users)) # type = list

print(users) # 확인
shuffle(users)
print(users) # 확인
chicken = users.pop() # 중복수령방지를 위해 리스트에서 제거
print("-- 당첨자 발표 --")
print("치킨 당첨자 :", chicken)
print("커피 당첨자 :", sample(users,3))
print("-- 축하합니다 --")

# -- solution --
users = range(1,21) # 1~21 '직전'까지!
print(type(users)) # type = range
users = list(users) #자료구조의 변경 -> list
print(type(users)) # type = list

winners = sample(users,4) # 4명 중에서 1명은 치킨, 3명은 커피

print(users) # 확인
shuffle(users)
print(users) # 확인
chicken = users.pop() # 중복수령방지를 위해 리스트에서 제거
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
