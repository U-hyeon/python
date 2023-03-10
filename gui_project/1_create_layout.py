# project) 여러 이미지를 합치는 프로그램을 만드시오.

# [사용자 시나리오]
# 1. 사용자는 합치려는 이미지를 1개 이상 선택한다.
# 2. 합쳐진 이미지가 저장될 경로를 지정한다.
# 3. 가로넓이, 간격, 포맷 옵션을지정한다.
# 4. 시작 버튼을 통해 이미지를 합친다.

# [기능 명세]
# 1. 파일추가 : 리스트 박스에 파일 추가
# 2. 선택삭제 : 리스트 박스에서 선택된 항목 삭제
# 3. 찾아보기 : 저장 폴더를 선택하면 텍스트 위젯에 입력
# 4. 가로넓이 : 이미지 넓이 지정 (원본유지, 1024, 800, 640)
# 5. 간격 : 이미지 간의 간격 지정 (없음, 좁게, 보통, 넓게)
# 6. 포맷 : 저장 이미지 포맷 지정(PNG, JPG, BMP)
# 7. 시작 : 이미지 합치기 작업 실행
# 8. 진행상황 : 현재 진행중인 파일 순서에 맞게 반영
# 9. 닫기 : 프로그램 종료

from tkinter import *

root = Tk()
root.title("Nado GUI")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가")
btn_add_file.pack(side="left")


btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제")
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # 높이변경
# ipad = inner padding 안쪽 영역크기변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right")

root.resizable(False, False)
root.mainloop()