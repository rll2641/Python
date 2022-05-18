class Graph_list:
    def __init__(self):
        self.vertex = None
        self.link = None

class Graph:
    def __init__(self):
        self.adj_list = [None] * 50
        self.node_size = 0
    
    def insert_vertex(self):
        self.node_size += 1
    
    def insert_edge(self, u, v):
        new_node = Graph_list()
        new_node.vertex = v
        new_node.link = self.adj_list[u]
        self.adj_list[u] = new_node
    
    def print_adj_list(self):
        for i in range(self.node_size):
            p = self.adj_list[i]
            print(f"vertex {i}`s near list", end=" ")
            while p != None:
                print("-> {0} ".format(p.vertex), end=" ")
                p = p.link
            print("")
            
g = Graph()

for i in range(4):
    g.insert_vertex()

g.insert_edge(0, 1);
g.insert_edge(1, 0);
g.insert_edge(0, 2);
g.insert_edge(2, 0);
g.insert_edge(0, 3);
g.insert_edge(3, 0);
g.insert_edge(1, 2);
g.insert_edge(2, 1);
g.insert_edge(2, 3);
g.insert_edge(3, 2);

g.print_adj_list()