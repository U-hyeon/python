# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로읽기, 한줄읽고 커서는 다음줄로 이동
# print(score_file.readline()) #줄별로읽기, 한줄읽고 커서는 다음줄로 이동
# print(score_file.readline()) #줄별로읽기, 한줄읽고 커서는 다음줄로 이동
# print(score_file.readline()) #줄별로읽기, 한줄읽고 커서는 다음줄로 이동
# score_file.close()

# # 파일이 몇줄인지 모를때
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # 모든 줄을 list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()