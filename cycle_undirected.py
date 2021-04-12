class Graph:
    def __init__(self,data):
        self.data = data

    def addEdge(self,u,v):
        if u in self.data.keys():
            u.append(v)
        else:
            self.data[u] = v

    def addVertex(self,n):
        if n not in self.data.keys():
            self.data[n] = []

    def printVertices(self):
        return list(self.data.keys())

    def printEdges(self):
        edge = []
        for i in self.data:
            for j in self.data[i]:
                if {i,j} not in edge:
                    edge.append({i,j})
        return edge

    def cycle(self):
        visited = []
        for i in self.data.keys():
            if i not in visited:
                if (self._cycle(i,visited,-1)) == True:
                    return True
        return False

    def _cycle(self,v,visited,parent):
        visited.append(v)
        for i in self.data[v]:
            if i not in visited:
                if self._cycle(i,visited,v):
                    return True
            elif parent != i:
                return True
        return False


graph = {'0':['1'],
'1':['0','2'],
'2':['1','3'],
'3':['2']
}

      
g = Graph(graph)

print(g.cycle())
        
