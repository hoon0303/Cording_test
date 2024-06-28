from sys import stdin
from itertools import product

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(routes, x,y,path):
    if len(path) == 4:
        routes.append(path[:])
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >=n or ny >= n:
            continue
        if (nx,ny) in path:
            continue
        path.append((nx,ny))
        dfs(routes, nx,ny,path)
        path.pop()

def total(comb):
    sum = 0
    visit = set()
    for c in comb:
        for l in c:

            x,y = l
            if (x,y) in visit:
                return 0
            visit.add((x,y))
            sum = sum + board[x][y]

    return sum
        
n,m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
friends = [list(map(int, stdin.readline().split())) for _ in range(m)]
friends_route = []
for friend in friends:
    routes = []
    x,y = friend
    dfs(routes,x-1,y-1,[(x-1,y-1)])
    friends_route.append(routes)

rst = 0
for comb in product(*friends_route):

    sum = total(comb)
    rst = max(rst, sum)
print(rst)