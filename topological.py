class Graph:
    def __init__(self,data):
        self.data = data

    def addVertex(self,data):
        if data not in self.data.keys():
            self.data[data] = []

    def addEdge(self,u,v):
        if u in self.data.keys():
            self.data[u].append(v)
        else:
            self.data[u] = [v]

    def printVertex(self):
        return list(self.data.keys())

    def printEdge(self):
        edge = []
        for i in self.data.keys():
            for j in self.data[i]:
                if {i,j} not in edge:
                    edge.append({i,j})
        return edge


    def topological(self):
        visited = []
        stack = []
        for i in self.data.keys():
            if i not in visited:
                self._topological(i,visited,stack)
        print(stack)
                

    def _topological(self,v,visited,stack):
        visited.append(v)
        for i in self.data[v]:
            if i not in visited:
                self._topological(i,visited,stack)
        stack.insert(0,v)

graph = {'5':['2','0'],
         '4':['0','1'],
         '0':[],
         '2':['3'],
         '3':['1'],
         '1':[]
}

g = Graph(graph)
print(g.printVertex())
print(g.printEdge())
g.topological()
