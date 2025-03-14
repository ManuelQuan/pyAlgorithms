import AbstractGraphSearcher
from AdjacencyList import AdjacencyList
import collections
class DepthFirstSearch:
    def __init__(self,graph,s):
        self.marked_list = [False] * (graph.vertex_count)
        self.edgeTo = [-1] * graph.vertex_count
        self.s = s
        self.count = 0
        self.__dfs(graph,s)
    
    def __dfs(self,graph,v):
        self.marked_list[v] = True
        self.count += 1
        for i in graph.graph[v]:
            if not self.marked_list[i]:
                self.edgeTo[i] = v
                self.__dfs(graph,i)

    def has_path_to(self,v):
        return self.marked_list[v]
    
    def count(self):
        return self.count
    
    def pathTo(self,v):
        if not self.has_path_to(v):
            return None
        path = collections.deque()
        x = v
        while(x!=self.s):
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.s)
        return path
if __name__ == "__main__":
    adj = AdjacencyList(6,8)
    searcher = DepthFirstSearch(adj,0)
    print(searcher.pathTo(3))
    