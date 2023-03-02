class Node:
    def __init__(self) -> None:
        self.edges_in = set()
        self.edges_out = set()

    def addEdgeIn(self, edge):
        self.edges_in.add(edge)
    
    def addEdgeOut(self, edge):
        self.edges_out.add(edge)

    def addEdgeBiDir(self, edge):
        self.edges_out.add(edge)
        self.edges_in.add(edge)
    
    def getEdgeIn(self):
        return self.edges_in

    def getEdgesOut(self):
        return self.edges_out
    
    def getEdgesBiDir(self):
        return self.edges_in.intersection(self.edges_out)


class Graph:
    def __init__(self):
        self.nodes = {}
    
    def addNode(self, node_key):
        self.nodes.update({node_key: Node()})

    def addNotValid(self, node_key):
        if node_key not in self.nodes.keys():
            self.addNode(node_key)

    def getNumNodes(self):
        return len(self.nodes)
    
    def getEdgesOut(self, key):
        return self.nodes[key].getEdgesOut()

    def getEdgesIn(self, key):
        return self.nodes[key].getEdgesOut()
    
    def getEdgesBiDir(self, key):
        return self.nodes[key].getEdgesBiDir()

    def addEdgeDir(self, a, b):
        self.addNotValid(a)
        self.addNotValid(b)
        self.nodes[a].addEdgeOut(b)
        self.nodes[b].addEdgeIn(a)

    def addEdgeBiDir(self, a, b):
        self.addNotValid(a)
        self.addNotValid(b)
        self.nodes[a].addEdgeBiDir(b)
        self.nodes[b].addEdgeBiDir(a)


def toposort_dfs(i, at, v, ordering, graph):
    v[at] = True

    edges = graph.getEdgesOut(at)

    for edge in edges:
        if v[edge] == False:
            i = toposort_dfs(i, edge, v, ordering, graph)
    
    ordering[i] = at
    return i - 1

def toposort(graph):
    n = graph.getNumNodes()
    v = [False for i in range(n)]
    ordering = [0 for i in range(n)]
    i=n-1

    for at in range(n):
        if v[at] == False:
            i = toposort_dfs(i, at, v, ordering, graph)
    return ordering

def dfs(v, graph):
    visited = []
    dfs_helper(v,graph,visited)
    return visited

def dfs_helper(v,graph,visited):
    visited.append(v)
    for edge in graph.getEdgesOut(v):
        if edge not in visited:
            dfs_helper(edge, graph, visited)
