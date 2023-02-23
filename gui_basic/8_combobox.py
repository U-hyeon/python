import tkinter.ttk as ttk # 콤보박스에 필요
from tkinter import *

root = Tk()

root.title("Nado GUI")
#root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표(왼쪽으로부터) + y좌표(위쪽에서부터)

values = [str(i) + "일" for i in range (1, 32)] # 1~31 까지의 숫자
# combobox = ttk.Combobox(root, height=5, values=values)
# combobox.pack()
# combobox.set("카드 결제일") # 최초 목록 제목 설정
# # 위 코드는 콤보박스에 임의의 텍스트를 입력후 버튼을 누르면 해당텍스트 출력, 오류의 원인

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 선택만 가능
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    # print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get()) # 선택된 값 표시


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()