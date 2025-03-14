import collections
import sys
class AdjacencyList:
    def __init__(self,*args,**kwargs):
        if len(args) == 1 and isinstance(args[0],int):
            self.vertex_count = args[0]
            self.edge_count = 0
            self.graph = collections.defaultdict(list)
        elif len(args) == 2 and isinstance(args[0],int) and isinstance(args[1],int):
            self.vertex_count = args[0]
            self.edge_count = 0
            self.graph = collections.defaultdict(list)
            for i in range(args[1]):
                user_input = input("input edge:")
                user_input_list = user_input.split(" ")
                v = int(user_input_list[0])
                w = int(user_input_list[1])
                print(f"{v},{w}")
                self.add_edge(v,w)

    def  add_edge(self,v,w):
        if(v > self.vertex_count or w > self.vertex_count):
            print("vertex idx out of range")
        self.graph[v].append(w)
        self.graph[w].append(v)
        self.edge_count += 1

    def printGraph(self):
        string_graph = f"{self.vertex_count} vertices, {self.edge_count} edges\n"
        for i in range(self.vertex_count):
            string_graph += f"{i}: "
            for j in self.graph[i]:
                string_graph += f"{j} "
            string_graph += "\n"
        return string_graph

if __name__ == "__main__":
    adj = AdjacencyList(13,13)
    print(adj.printGraph())



