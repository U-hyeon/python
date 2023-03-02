from tkinter import *

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표(왼쪽으로부터) + y좌표(위쪽에서부터)

Label(root, text="메뉴를 선택해 주세요").pack(side="top") # 프레임은 위로 붙는다

Button(root, text="주문하기").pack(side="bottom") # 프레임은 아래로 붙는다

# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1) # bd : 외곽선
frame_burger.pack(side="left", fill="both", expand=True) # 왼쪽붙고, 양쪽채우고 확장

Button(frame_burger, text="햄버거").pack() # root 가 아닌 frame_burger에 포함
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료") # frame 명칭 "음료"
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack() # root 가 아닌 frame_drink에 포함
Button(frame_drink, text="사이다").pack()


root.mainloop()