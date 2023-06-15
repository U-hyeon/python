# Quiz) tkinter 를 이용한 메모장 프로그램을 만드시오

# [GUI 조건]
# 1. title : 제목없음 - Windows 메모장
# 2. 메뉴 : 파일 편집 서식 보기 도움말
# 3. 실제메뉴구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기

import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog

file_name = "제목없음"

root = Tk()
root.title(file_name + "- Windows 메모장")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x")

# ------------------------
# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
# 본문
txt = Text(root, yscrollcommand=scrollbar.set) # 5줄
txt.pack(side="left", fill="both", expand=True)
# 매핑
scrollbar.config(command=txt.yview)

# -------------------
# 상단메뉴

def file_open():
    # mynote.txt 열어서 보여주기
    files = filedialog.askopenfilenames(title="열기", \
            filetypes=(("txt 파일", "*.txt"), ("모든 파일", "*.*")), \
            initialdir=".") 
    # 최초에 "사용자가 지정한" 경로를 보여줌
    global full_name
    full_name = str(files)
    full_name = full_name[2:-3]
    dir_names = full_name.split('/')
    print(dir_names)
    file_name = dir_names[len(dir_names) - 1]
    if not os.path.isfile(full_name):
        msgbox.showerror("에러", "파일이 존재하지 않습니다.")
    elif not full_name[-4:] == ".txt":
        # .txt 파일이 아니라면 중단
        msgbox.showerror("에러", "텍스트 파일을 선택하세요.")
    else:
        # 사용자가 선택한 파일명으로 title 갱신
        print(type(files), file_name)
        root.title(file_name + "- Windows 메모장")
        # print(full_name)
        # 파일 열기
        with open(full_name, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력
    
def file_save():
    print("save into:",full_name)
    with open(full_name, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

def file_saveinto():
    pass
    filedialog.asksaveasfilename

menu = Menu(root) # 메뉴

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=file_open)
menu_file.add_command(label="저장", command=file_save)
menu_file.add_command(label="다른 이름으로 저장", command=file_saveinto)
menu_file.add_separator() # 경계선 ----------
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file) # menu에 menu_file정보를 삽입

menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit) # menu에 menu_edit정보를 삽입

menu_layout = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_layout) # menu에 menu_layout정보를 삽입

menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_view) # menu에 menu_view정보를 삽입

menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_help) # menu에 menu_help정보를 삽입

root.config(menu=menu) # 메뉴

# root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표(왼쪽으로부터) + y좌표(위쪽에서부터)
# root.resizable(True, True) # x(너비), y(높이) 값 변경불가 (창 크기)False, False)
root.mainloop()