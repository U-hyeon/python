#애완동물을 소개해 주세요

animal = "강아지" #string
name = "연탄이" #string
age = 4 #int
hobby = "산책" #string
is_adult = age >= 3 #bool

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, "+ hobby +"을 아주 좋아해요") #정수형 표현할때는 str(int)
print(name, "는 ", age, "살이며, ", hobby ,"을 아주 좋아해요") 
# + 대신 ,를 사용해도 된다. 이때는 str(int)로 묶지않아도 됨. 
# #연결부위마다 띄어쓰기가 하나씩 추가됨
print(name + "는 어른일까요? " + str(is_adult))

'''
작은따옴표 3개를 통해 여러문장을 주석처리
'''

# 원하는구간 스크롤후 "ctrl + /"로 일괄주석 & 해제

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, "+ hobby +"을 아주 좋아해요") #정수형 표현할때는 str(int)
print(name, "는 ", age, "살이며, ", hobby ,"을 아주 좋아해요") 
# + 대신 ,를 사용해도 된다. 이때는 str(int)로 묶지않아도 됨. 
# #연결부위마다 띄어쓰기가 하나씩 추가됨
print(name + "는 어른일까요? " + str(is_adult))
