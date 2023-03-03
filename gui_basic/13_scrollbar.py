from tkinter import *

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표(왼쪽으로부터) + y좌표(위쪽에서부터)

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set을 안하면 스크롤을 내려도 다시 올라옴. 동작안함
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set)

for i in range(1,32): # 1~31일
    listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack()

# 스크롤바에서도 설정해야함
scrollbar.config(command=listbox.yview)

root.mainloop()