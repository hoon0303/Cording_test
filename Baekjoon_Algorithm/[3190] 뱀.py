
from collections import deque

time = [0] * 10000

N = int(input())
K = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

board = [[0] * N for _ in range(N)]

for i in range(K):
    x,y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input())
for i in range(L):
    x,y = input().split()
    x= int(x)
    time[x] = y

def bfs(x,y):
    q = deque()
    q.append((x,y))
    pos = 0
    nx = x
    ny = y
    cnt = -1
    while(True):
        

        cnt= cnt + 1
        if time[cnt] == 'D':
            pos = (pos + 1) % 4
        if time[cnt] == 'L':
            pos = (pos - 1) % 4

        nx = dx[pos] + nx
        ny = dy[pos] + ny

        if nx < 0 or ny < 0 or nx >=N or ny >= N:
            return cnt
        if (nx,ny) in q:
            return cnt

        if board[nx][ny] == 1:
            board[nx][ny] = 0
            q.append((nx,ny))
        else:
            q.append((nx,ny))
            q.popleft()


x = bfs(0,0)
print(x)