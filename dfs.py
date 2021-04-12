class Graph:
    def __init__(self,data):
        if data is None:
            data = []
        else:
            self.data = data

    def addVertex(self,n):
        self.data[n] = [] 

    def addEdge(self,u,v):
        if u not in self.data:
            self.data[u] = [v]
        else:
            self.data[u].append(v)

    def printVertices(self):
        return self.data.keys()

    def printEdges(self):
        edge = []
        for i in self.data:
            for j in self.data[i]:
                edge.append({i,j})
        return edge

    def dfs(self,visited,x):
        if x not in visited:
            print(x)
            visited.append(x)
            for i in self.data[x]:
                self.dfs(visited,i)


graph = { "a" : ["b","c"],
      "b": ["a","d"],
      "c": ["a","d"],
      "d": ["e"],
      "e": ["d"]
    }
g = Graph(graph)
g.dfs([],'a')

