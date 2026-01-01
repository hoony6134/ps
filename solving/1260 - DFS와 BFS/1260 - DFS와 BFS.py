# BOJ 1260 - DFS와 BFS
class Graph:
    adj = []

    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.adj = [[0 for _ in range(v + 1)] for _ in range(v + 1)]

    def addEdge(self, start, e):
        self.adj[start][e] = 1
        self.adj[e][start] = 1

    def bfs(self, start):
        visited = [False] * (self.v + 1)
        q = [start]
        visited[start] = True
        while q:
            vis = q[0]
            print(vis, end=" ")
            q.pop(0)
            for i in range(self.v):
                if self.adj[vis][i] == 1 and (not visited[i]):
                    q.append(i)
                    visited[i] = True

    def dfs(self, start, visited):
        print(start, end=" ")
        visited[start] = True
        for i in range(self.v):
            if self.adj[start][i] == 1 and (not visited[i]):
                self.dfs(i, visited)


v, e, i = map(int, input().split())
G = Graph(v, e)
for _ in range(e):
    a, b = map(int, input().split())
    G.addEdge(a, b)

G.dfs(i, [False] * (v + 1))
print()
G.bfs(i)
