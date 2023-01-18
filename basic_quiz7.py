# import pickle

# quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# ---본인답안
# 주차 = 1
# 부서 = "인사과"
# 이름 = "kevin"
# 업무요약 = "특이사항없음"

# with open("{0} 주차.txt".format(주차), "w", encoding="utf8") as study_file:
#     study_file.write("- {0} 주차 주간보고 -\n".format(주차))
#     study_file.write("부서 : {0}\n".format(부서))
#     study_file.write("이름 : {0}\n".format(이름))
#     study_file.write("업무 요약 : {0}\n".format(업무요약)) # 파일작성

# with open("{0} 주차.txt".format(주차), "r", encoding="utf8") as study_file:
#     print(study_file.read())

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")