from lib_graph import Graph, dfs

n,m = map(int,input().split())
# n rows, m cols

lis = []


grid = []

for i in range(n):
    grid.append(list(input()))

# print(grid)

g = Graph()

for i in range(n):
    for j in range(m):
        if grid[i][j] != "W":
            if grid[i][j] == "L":
                lis.append(i*m + j)
                g.addNode(i*m + j)
            if i+1 < n and grid[i+1][j] != "W":
                g.addEdgeDir(i*m + j, (i+1)*m + j)
            if i-1 >= 0 and grid[i-1][j] != "W":
                g.addEdgeDir(i*m + j, (i-1)*m + j)
            if j+1 < m and grid[i][j+1] != "W":
                g.addEdgeDir(i*m + j, i*m + j + 1)
            if j-1 >= 0 and grid[i][j-1] != "W":
                g.addEdgeDir(i*m + j, i*m + j-1)

islands = 0 
while len(lis) != 0:
    # print(lis)
    connects = dfs(lis[0], g)
    for connect in connects:
        if connect in lis:
            lis.remove(connect)
    islands+=1

print(islands)