python = "Python is Amazing"
print(python.lower()) # 소문자로 출력
print(python.upper()) # 대문자로 출력
print(python[0].isupper()) # 0번항이 대문자인가 T/F
print(len(python)) # 길이반환
print(python.replace("Python", "Java")) # A문자열을 B문자열로 치환

index = python.index("n") # 해당 문자열의 첫번째 항 번호
print(index)
index = python.index("n", index + 1) # 그 다음 항 번호
print(index)

print(python.find("Java")) # 원하는 값이 없으면 -1 반환
# print(python.index("Java")) # 원하는 값이 없으면 error 출력후 '종료'
print("hi")

print(python.count("n")) # 해당 문자열이 총 몇번 등장하는지 반환