kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # *이 붙으면 분리 unzip

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)