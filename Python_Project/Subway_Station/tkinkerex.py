from tkinter import *
import tkinter
import subway_bfs as sb

subway = Tk()
subway.title("지하철 최단경로")
subway.geometry("800x500")
subway_img = tkinter.PhotoImage(file="지하철.png")
label = tkinter.Label(subway, image=subway_img)
label.place(x=0, y=0)

# 출발열 입력
input_start = Entry(subway)
input_start.place(x=580, y=30)
def receive_start():
    st = input_start.get()
    

# 출발열 선택 버튼
btn_start = Button(subway, text="출발역 선택")
btn_start.config(width=10, height=2)
btn_start.config(command=receive_start)
btn_start.place(x=610, y=50)

# 도착역
input_end = Entry(subway)
input_end.place(x=580, y=120)
def receive_end():
    ed = input_end.get()
    
# 도착열 선택 버튼
btn_end = Button(subway, text="도착역 선택")
btn_end.config(width=10, height=2)
btn_end.config(command=receive_end)
btn_end.place(x=610, y=140)

label2 = Label(subway)
label2.place(x=550, y=300)
def bfs_start():
    result = sb.bfs(input_start.get(), input_end.get())
    label2.configure(text= "경로: "+"->".join(result))

# 최단 경로 시작
btn3 = Button(subway, text="최단 경로")
btn3.config(width=10, height=2)
btn3.config(command=bfs_start)
btn3.place(x=610, y=200)

subway.mainloop()