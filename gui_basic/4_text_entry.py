from tkinter import *

root = Tk()

root.title("Nado GUI")
#root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표(왼쪽으로부터) + y좌표(위쪽에서부터)

txt = Text(root, width=30, height=5) # 5줄
txt.pack()

txt.insert(END, "글자를 입력하세요") # 끝부분에 기본입력값

e=Entry(root, width=30) # 1줄짜리, 엔터불가
e.pack()
e.insert(0, "한 줄만 입력해요") # 처음위치에 기본입력값

def btncmd():
    #콘솔로 내용출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())
    #텍스트박스 내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()