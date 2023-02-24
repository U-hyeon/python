import tkinter.ttk as ttk # progress bar 에 필요
import time
from tkinter import *

root = Tk()

root.title("Nado GUI")
#root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표(왼쪽으로부터) + y좌표(위쪽에서부터)


# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 끝을모르고 왕복
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 끝까지가면 초기화
progressbar.start(10) # 10 ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # 작동 중지

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i)
        progressbar2.update() # 한번의 루프마다 gui 업데이트
        print("진행도", p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()