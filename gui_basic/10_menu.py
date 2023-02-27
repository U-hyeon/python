from tkinter import *

root = Tk()
root.title("Nado GUI")
#root.geometry("640x480") # 가로 x 세로
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표(왼쪽으로부터) + y좌표(위쪽에서부터)

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root) # 메뉴

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 경계선 ----------
menu_file.add_command(label="Open File...")
menu_file.add_separator() # 경계선 ----------
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file) # menu에 menu_file정보를 삽입

# Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

#Language 메뉴 추가 (radio 버튼을 통해서 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu) # 메뉴
root.mainloop()