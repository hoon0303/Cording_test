

import sys

dx = [-1,0,1,0]
dy = [0,1,0,-1]
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
cnt = 0
def dfs(r,c,d):
    global cnt
    p=d
    if board[r][c] == 0 and visit[r][c] == 0:
        cnt = cnt + 1
        visit[r][c] = 1

    for i in range(4):
        p = (p+3) % 4
        nx = r + dx[p]
        ny = c + dy[p]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if board[nx][ny] == 0 and visit[nx][ny] == 0:
            dfs(nx,ny,p)
            return
    nx = r - dx[p]
    ny = c - dy[p]
    if board[nx][ny] != 1:
        dfs(nx, ny , p)


dfs(r,c,d)
print(cnt)
