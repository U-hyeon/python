from tkinter import *

# label : 그림, 이미지만 보여준다. 기능x

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change(): # change 함수 정의
    label1.config(text="또 만나요")
    # 기존이미지가 삭제되고 새 이미지 출력안됨 - garbage collection 문제 - 함수종료후 해당 지역변수가 사라지기때문
    global photo2 # 전역변수로 설정해야 제대로 변경된다.
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change) # 버튼에 change함수 할당
btn.pack()

root.mainloop()