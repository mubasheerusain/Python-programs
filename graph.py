class graph:
    def __init__(self,data = None):
        if data is None:
            data = []
        self.data = data

    def getVertices(self):
        return list(self.data.keys())

    def edge(self):
        return self.findedge()

    def findedge(self):
        edge = []
        for v in self.data:
            for v1 in self.data[v]:
                if {v,v1} not in edge:
                    edge.append({v,v1})
        return edge

    def addVertex(self,data):
        if data not in self.data:
            self.data[data] = []

    def addEdge(self,edge):
        edge = set(edge)
        (vertex1,vertex2) = tuple(edge)
        if vertex1 in self.data:
            self.data[vertex1].append(vertex2)
        else:
            self.data[vertex1] = [vertex2]



g = { "a" : ["b","c"],
      "b": ["a","d"],
      "c": ["a","d"],
      "d": ["e"],
      "e": ["d"]
    }
Graph = graph(g)
print(Graph.getVertices())
print(Graph.edge())
Graph.addVertex("f")
print(Graph.getVertices())
Graph.addEdge({'a','e'})
Graph.addEdge({'a','c'})
print(Graph.edge())
