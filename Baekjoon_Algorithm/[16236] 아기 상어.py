from collections import deque
import copy

dx = [-1,0,0,1]
dy = [0,-1,1,0]

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def bfs(x1,y1,size):

    visit = [[0] * N for _ in range(N)]
    q = deque()
    q.append((x1,y1))
 
    visit[x1][y1] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if board[nx][ny] > size:
                continue
            if board[nx][ny] < size and board[nx][ny] != 0:
                board[nx][ny] = 0
                return nx,ny,visit[x][y] + 1
            
            if visit[nx][ny] == 0:
                q.append((nx,ny))
                visit[nx][ny] = visit[x][y] + 1

    return x1,y1,0

def func():
    size = 2
    time = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                nx = i
                ny = j
                break
    while True:
        x1,y1,c = bfs(nx,ny,size)
        time = time + c
        if c == 0:
            print(time)
            return
        cnt = cnt + 1
        if size == cnt:
            size = size + 1
            cnt = 0
        nx = x1
        ny =y1
func()