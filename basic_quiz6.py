# quiz) 표준 체중을 구하는 프로그램을 작성하시오

# *표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     *함수명 : std_weight
#     *전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자" :
        return round( (height/100) * (height/100) * 22, 2 ) #round(num, where)
    elif gender == "여자" :
        return round( (height/100) * (height/100) * 21, 2 ) #round(num, where) 소수점 자리지정
    else :
        return "error!"

def print_std_weight(height, gender):
    print("키 {0}{1}의 표준 체중은 {2}입니다.".format(height, gender, std_weight(height, gender)))

print_std_weight(175, "남자")
print_std_weight(160, "여자")
print_std_weight(180, "중성마녀")
