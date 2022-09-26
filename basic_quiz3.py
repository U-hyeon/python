# 사이트별로 비밀번호를 만들어 주는 프로그램
# 예)http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성
#                    (nav)            (5)            (1)           (!)
# 생성된 비밀번호 : nav51!

#주소 = "http://naver.com"
#주소 = "http://daum.net"
주소 = "http://google.com"

#tmp = 주소[7 : 주소.find(".")] # http:// 제외, 처음만난 점(.) 이후부분 제외
tmp = 주소.replace("http://", "") # http:// 제외
print(tmp)
tmp = tmp[:tmp.index(".")] # 처음만난 점(.) 이후부분 제외
print(tmp)
password = tmp[:3] + str(len(tmp)) + str(tmp.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(주소, password))