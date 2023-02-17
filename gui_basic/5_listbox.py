from tkinter import *

root = Tk()

root.title("Nado GUI")
#root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표(왼쪽으로부터) + y좌표(위쪽에서부터)

listbox = Listbox(root, selectmode="extended", height=0) # height = 0일때: 전체크기만큼 출력
# height !=0 일때: 지정된 크기만큼만 표시 (스크롤바)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #listbox.delete(0) # 맨 앞 항목을 삭제
    #listbox.delete(END) # 맨 뒤 항목을 삭제
    
    #갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요")
    
    #항목 확인 get(시작 index, 끝 index)
    #print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))

    #선택된 항목 확인 (index로 표시)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()