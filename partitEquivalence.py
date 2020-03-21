import numpy as np

def buildGraph(verts, edges):
    graph = {v:set() for v in verts}
    for a,b in edges:
        graph[a].add(b)
        graph[b].add(a)
    return graph

def DFStraverse(graph, node, unvisited):
    visited = set()
    
    def visitNode(node):
        visited.add(node)
        unvisited.remove(node)
        for child in graph[node]:
            if child in unvisited:
                visitNode(child)
    visitNode(node)
    
    return visited, unvisited

from collections import deque

def BFStraverse(graph, node, unvisited):
    visited = set()
    queue = deque()
    
    queue.append(node)
    visited.add(node)
    unvisited.remove(node)
    
    while queue:
        n = queue.popleft()
        
        for child in graph[n]:
            if child not in visited:
                queue.append(child)
                visited.add(child)
                unvisited.remove(child)
    
    return visited, unvisited

class partitEquivalence:
    def __init__(self, pairs, eles=None):
        self.pairs = np.unique(np.array(pairs),axis=0)
        self.eles = eles if eles is None else np.unique(np.array(pairs))
        self.eles.sort()
        self.graph = None
        self._equivalence = []
        
    def buildGraph(self):
        self.graph = buildGraph(self.eles, self.pairs)
 
    def partition(self):
        unvisited = set(self.eles)
        while unvisited:
            visited, unvisited = BFStraverse(self.graph, next(iter(unvisited)), unvisited)
            self._equivalence.append(visited)
    @property
    def equivalence(self):
        if self._equivalence:
            return self._equivalence
        else:
            self.buildGraph()
            self.partition()
            return self._equivalence