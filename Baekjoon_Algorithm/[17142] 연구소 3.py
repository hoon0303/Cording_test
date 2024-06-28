from collections import deque
from itertools import combinations
INF = float('inf') #임의의 큰 수
N, M = map(int, input().split())
dx = [0,0,1,-1]
dy = [-1,1,0,0]

board = [ list(map(int, input().split())) for _ in range(N)]

birus = []
blank = 0
def find():
    global blank
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                birus.append((i,j))
            if board[i][j] == 0:
                blank = blank + 1
    
find()

birus_list = list(combinations(birus,M))

def bfs(birus_list, blank):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for birus in birus_list:
        q.append(birus)
        x,y = birus
        visited[x][y] = 1

    cnt  = 0
    while True:
        if blank == 0 or len(q) == 0:
            if blank == 0:
                return cnt
            else:
                return INF


        cnt  = cnt+1

        for i in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if board[nx][ny] == 1 or visited[nx][ny] == 1:
                    continue
                
                if board[nx][ny] == 0:
                    blank = blank - 1
                    q.append((nx,ny))
                    visited[nx][ny] = 1


                if board[nx][ny] == 2:
                    q.append((nx,ny))
                    visited[nx][ny] = 1


m = INF
for birus in birus_list:
    x = bfs(birus, blank)
    m = min(m,x)


if m == INF:
    print(-1)

else:
    print(m)