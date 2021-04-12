class Graph:
    def __init__(self,data = None):
        if data is None:
            data = []
        self.data = data

    def bfs(self,n):
        visited = []
        queue = []
        visited.append(n)
        queue.append(n)
        while queue:
            s = queue.pop(0)
            print(s)
            for i in self.data[s]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)

    def printEdge(self):
        edge = []
        for i in self.data:
            for j in self.data[i]:
                if {i,j} not in edge:
                    edge.append({i,j})
        return edge

    def printVertex(self):
        return list(self.data.keys())

    def addVertices(self,n):
        if n not in self.data:
            self.data[n] = []  

    def addEdge(self,x,y):
        if x in self.data:
            self.data[x].append(y)
        else:
            self.data[x] = [y]


graph = { "a" : ["b","c"],
      "b": ["a","d"],
      "c": ["a","d"],
      "d": ["e"],
      "e": ["d"]
    }
g = Graph(graph)
g.addVertices('f')
g.bfs('a')
print(g.printVertex())
print(g.printEdge())

