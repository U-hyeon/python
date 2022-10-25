print("Python", "Java", sep=",", end="?") 
print("무엇이 더 재밌을까요?")
# sep(seperate)를 이용하여 각 변수 사이에 들어갈 문자지정 (기본 : space)
# end를 이용하여 출력끝부분에 들어갈 문자지정 (기본 : 줄바꿈)

# import sys
# print("Python", "Java", file=sys.stdout) #표준출력
# print("Python", "Java", file=sys.stderr) #표준에러

# scores = {"수학":0, "영어":50, "코딩":100} # dictionary
# for subject, score in scores.items(): # items > key, value 쌍으로 반환
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") 
#     # ljust(i) : i칸을 확보하고 왼쪽정렬, rjust 오른쪽정렬

# #은행 대기순번표
# # 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) 
#     # zfill(i) > i칸만큼 확보하고 빈칸은 0(zero)를 채워라

answer = input("아무 값이나 입력하세요 : ") 
# 사용자 입력으로 받은 값은 항상 string
# answer = 10 # int
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")