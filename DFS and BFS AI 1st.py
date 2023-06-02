from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = {}
        for i in range(n):
            self.adjList[i] = []
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

    def recBFS(self, q, discovered):
        if not q:
            return
        v = q.popleft()
        print(v, end=" ")
        for u in self.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)
        self.recBFS(q, discovered)

    def DFSrec(self, v, discovered):
        print(v, end=" ")
        for u in self.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                self.DFSrec(u, discovered)

if __name__ == '__main__':
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    n = 7
    graph = Graph(edges, n)
    discovered = [False] * n
    q = deque()
    print("Recursive BFS ->")
    for i in range(n):
        if not discovered[i]:
            discovered[i] = True
            q.append(i)
            graph.recBFS(q, discovered)

    print("\nRecursive DFS ->")
    discovered = [False] * n
    discovered[0] = True
    graph.DFSrec(0, discovered)