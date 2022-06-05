from tkinter import *
from tkinter.font import Font
import tkinter

import subway_bfs as sb
import subway_dijkstra as sd

# 타이틀 이름, 크기
subway = Tk()
subway.title("지하철 최단경로")
subway.geometry("1400x900")

# 이미지 불러오기
subway_img = tkinter.PhotoImage(file="지하철.png")
label = tkinter.Label(subway, image=subway_img)
label.place(x=0, y=0)

# 폰트 변경
subway_font = Font(size=18)

# 출발열 입력
input_start = Entry(subway)
input_start.place(x=1050, y=30, width=200, height=50)
input_start.configure(font=subway_font)
def receive_start():
    st = input_start.get()
    
# 출발열 선택 버튼
btn_start = Button(subway, text="출발역 선택")
btn_start.config(width=10, height=2)
btn_start.config(command=receive_start)
btn_start.place(x=1100, y=80)

# 도착역
input_end = Entry(subway)
input_end.place(x=1050, y=150, width=200, height=50)
input_end.configure(font=subway_font)
def receive_end():
    ed = input_end.get()
    
# 도착열 선택 버튼
btn_end = Button(subway, text="도착역 선택")
btn_end.config(width=10, height=2)
btn_end.config(command=receive_end)
btn_end.place(x=1100, y=200)

# 최단 경로 출력
label_bfs = Label(subway)
label_bfs.place(x=950, y=400)
def bfs_start():
    result = sb.bfs(input_start.get(), input_end.get())
    label_bfs.configure(text="경로:" + "->".join(result), wraplength=300, font=subway_font)
    
# 최단 경로 시작
btn_bfs = Button(subway, text="최단 경로")
btn_bfs.config(width=10, height=2)
btn_bfs.config(command=bfs_start)
btn_bfs.place(x=1070, y=300)

# 최단 거리 출력
label_dijk = Label(subway)
label_dijk.place(x=950, y=600)
def dijk_start():
    result = sd.dijkstra(input_start.get())
    label_dijk.configure(text="거리: " + str(round(result[input_end.get()], 2)) + "km", font=subway_font)
    
# 최단 거리
btn_dijk = Button(subway, text="최단 거리")
btn_dijk.config(width=10, height=2)
btn_dijk.config(command=dijk_start)
btn_dijk.place(x=1150, y=300)


subway.mainloop()