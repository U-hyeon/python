print("a" + "b")
print("a", "b")

#방법1
print("나는 %d살입니다." % 20) # %d : 정수
print("나는 %s을 좋아해요." % "파이썬") # %s : 스트링
print("Apple 은 %c로 시작해요." % "A") # %c : 한 character
# %s (만능)
print("나는 %s살입니다." % 20) # %d : 정수
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) #두가지 이상의 값 : ()

#방법2
print("방법2")
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간")) #두가지 이상의 값 : ()
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간")) #두가지 이상의 값 : ()
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간")) #{숫자} : 순서 설정

# 방법3
print("방법3")
print("나는 {age}살이며, {color}색을 좋아해요.".format (age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format (color = "빨간", age = 20))

#방법4
print("방법4")
age=20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")