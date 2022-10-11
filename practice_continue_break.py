# continue : ex) 결석한 번호 건너뛰기
absent = [2,5] #결석
no_book = [7] #책을 깜빡했음
for student in range(1,11) : # 1~10
    if student in absent: #결석했다면
        continue #밑의 명령 무시하고 다음 loop로 이동
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format (student))
        break #loop 탈출
    print("{0}, 책을 읽어봐".format(student))