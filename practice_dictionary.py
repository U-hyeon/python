# 단어 - 뜻 관계처럼
# key : value 사전자료형
cabinet = {3: "유재석", 100: "김태호"} #중괄호.
#방법1
print(cabinet[3])
print(cabinet[100])
#방법2
print(cabinet.get(3))
print(cabinet.get(100))

print(cabinet.get(5)) # None 출력
print(cabinet.get(5), "사용가능") # 5번이 비었으면 "사용가능" 출력
print("hi")
# error
#print(cabinet[5]) # 대괄호는 오류출력후 강제종료
#print("hi")

# 값이 있는지 확인 (key in 자료형)
print(3 in cabinet) # true
print(5 in cabinet) # false

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 이미 사용중인 키
cabinet["C-20"] = "조세호" # 사용하지 않는 키
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)