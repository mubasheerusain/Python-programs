class Graph:
    def __init__(self,data):
        self.data = data

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
        stack = []
        for i in self.data.keys():
            if i not in visited:
                if (self._cycle(i,visited,stack)) == True:
                    return True
        return False

    def _cycle(self,v,visited,stack):
        visited.append(v)
        stack.append(v)
        for i in self.data[v]:
            if i not in visited:
                if self._cycle(i,visited,stack):
                    return True
            elif i in stack:
                return True
        stack.pop()
        return False


graph ={ "0" : ["1","2"],
      "1": ["2"],
      "2": ["3","0"],
      "3": ["3"]
      }
graph1 ={ "0" : ["1","2"],
      "1": ["2"],
      "2": ["3"],
      "3": []
      }
g = Graph(graph1)
print(g.printVertices())
print(g.printEdges())
print(g.cycle())
