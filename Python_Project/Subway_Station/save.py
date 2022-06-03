from collections import deque

from pkg_resources import parse_requirements

station_bgraph = { 
    '용산': ['이촌'],
    '이촌': ['서빙고', '동작', '용산'],
    '서빙고': ['이촌', '한남'],
    '한남': ['서빙고', '옥수'],
    '옥수': ['한남', '압구정'],
    '흑석': ['동작'],
    '동작': ['흑석', '구반포', '총신대입구', '이촌'],
    '구반포': ['동작', '신반포'],
    '신반포': ['구반포', '고속터미널'],
    '고속터미널': ['신반포', '잠원', '교대', '내방'],
    '압구정': ['옥수', '신사'],
    '신사': ['압구정', '잠원'],
    '잠원': ['신사', '고속터미널'],
    '총신대입구': ['동작', '내방', '사당'],
    '내방': ['총신대입구', '고속터미널'],
    '사당': ['총신대입구', '방배'],
    '방배': ['사당', '서초'],
    '서초': ['방배', '교대'],
    '교대': ['서초', '고속터미널']
}

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in station_bgraph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

from tkinter import *
import tkinter
import subway_bfs as sb

subway = Tk()
# 타이틀 제목
subway.title("지하철 최단경로")
# 창 크기
subway.geometry("800x500")
# 이미지 저장
subway_img = tkinter.PhotoImage(file="지하철3.png")
# 이미지 불러오기
label = tkinter.Label(subway, image=subway_img)
label.place(x=0, y=0)

# 출발열 입력
input_start = Entry(subway)
input_start.place(x=580, y=100)
def ent():
    s = input_start.get()
    print(s)
    print(type(s)) # str
    
# 출발열 선택 버튼
btn = Button(subway, text="출발역 선택")
btn.config(width=10, height=2)
btn.config(command=ent)
btn.place(x=610, y=120)

# 도착역
input_end = Entry(subway)
input_end.place(x=580, y=200)
def ent():
    s = input_end.get()
    print(s)
    print(type(s)) # str
    
# 도착열 선택 버튼
btn2 = Button(subway, text="도착역 선택")
btn2.config(width=10, height=2)
btn2.config(command=ent)
btn2.place(x=610, y=220)

# 최단 거리 시작
btn4 = Button(subway, text="최단 경로")
btn4.config(width=10, height=2)
btn4.config(command=ent)
btn4.place(x=560, y=300)

# 최단 경로 시작
btn3 = Button(subway, text="최단 경로")
btn3.config(width=10, height=2)
btn3.config(command=ent)
btn3.place(x=640, y=300)

subway.mainloop()