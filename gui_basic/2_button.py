from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2") # padx, pady : 버튼여백증가
btn2.pack()
btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()
btn4 = Button(root, width=10, height=3, text="버튼4") #width, height : 고정된크기, 텍스트길이가길면 짤림
btn4.pack()
btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg: 글자색, bg: 배경색
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png") # 이미지 출력
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는버튼", command=btncmd) # 명령할당
btn7.pack()

root.mainloop()