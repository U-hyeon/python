#자료구조의 변경
#커피숍
menu = {"커피", "우유", "주스"} # set - 중괄호
print(menu, type(menu))

menu = list(menu) # list로 변경 - 대괄호
print(menu, type(menu))

menu = tuple(menu) # tuple로 변경 - 소괄호
print(menu, type(menu))

menu = set(menu) # set로 변경 - 중괄호
print(menu, type(menu))
