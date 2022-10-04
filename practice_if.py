# weather = "비"
# weather = "미세먼지"
# weather = "맑음"
# weather = input("오늘 날씨는 어때요? ") # 메시지 출력후 입력대기

# # if 조건 :
# #    실행 명령문

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30: # and 를 이용한 복수조건
    print("괜찮은 날씨에요")
elif 0 <= temp < 10: # 한번에 적는 복수조건
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")