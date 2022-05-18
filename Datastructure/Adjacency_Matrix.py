class Graph:
    def __init__(self):
        self.adj_mat = [[0]*50 for _ in range(50)]
        self.node_size = 0
    
    def insert_vertex(self):
        self.node_size += 1
    
    def insert_edge(self, start, end):
        self.adj_mat[start][end] = 1
        self.adj_mat[end][start] = 1
        
    def print_adj_mat(self):
        for i in range(self.node_size):
            for j in range(self.node_size):
                print(self.adj_mat[i][j], end=" ")
            print("")

g = Graph()

for i in range(4):
    g.insert_vertex()

g.insert_edge(0, 1)
g.insert_edge(0, 2)
g.insert_edge(0, 3)
g.insert_edge(1, 2)
g.insert_edge(2, 3)

g.print_adj_mat()