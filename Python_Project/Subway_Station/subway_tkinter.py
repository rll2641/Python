from tkinter import *
import tkinter
import subway_bfs as sb
import subway_dijkstra as dijk

subway = Tk()
subway.title("지하철 최단경로")
subway.geometry("900x500")
subway_img = tkinter.PhotoImage(file="지하철.png")
label = tkinter.Label(subway, image=subway_img)
label.place(x=0, y=0)

# 출발열 입력
input_start = Entry(subway)
input_start.place(x=630, y=30)
def receive_start():
    st = input_start.get()
    
# 출발열 선택 버튼
btn_start = Button(subway, text="출발역 선택")
btn_start.config(width=10, height=2)
btn_start.config(command=receive_start)
btn_start.place(x=660, y=50)

# 도착역
input_end = Entry(subway)
input_end.place(x=630, y=120)
def receive_end():
    ed = input_end.get()
    
# 도착열 선택 버튼
btn_end = Button(subway, text="도착역 선택")
btn_end.config(width=10, height=2)
btn_end.config(command=receive_end)
btn_end.place(x=660, y=140)

# 최단 경로 출력
label_bfs = Label(subway)
label_bfs.place(x=520, y=300)
def bfs_start():
    result = sb.bfs(input_start.get(), input_end.get())
    label_bfs.configure(text="경로:" + "->".join(result), wraplength=300)
    
# 최단 경로 시작
btn_bfs = Button(subway, text="최단 경로")
btn_bfs.config(width=10, height=2)
btn_bfs.config(command=bfs_start)
btn_bfs.place(x=680, y=200)

# 최단 거리 출력
label_dijk = Label(subway)
label_dijk.place(x=520, y=400)
def dijk_start():
    result = dijk.dijkstra(input_start.get())
    label_dijk.configure(text="거리: " + str(result[input_end.get()]) + "km")
    
# 최단 거리
btn_dijk = Button(subway, text="최단 거리")
btn_dijk.config(width=10, height=2)
btn_dijk.config(command=dijk_start)
btn_dijk.place(x=600, y=200)


subway.mainloop()