from tkinter import *

root = Tk()

root.title("Nado GUI")
#root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표(왼쪽으로부터) + y좌표(위쪽에서부터)
root.resizable(False, False) # x(너비), y(높이) 값 변경불가 (창 크기)

root.mainloop()