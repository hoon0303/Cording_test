from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def g_bfs(start_positions, g_board):
    q = deque()
    for x, y in start_positions:
        q.append((x, y))
        g_board[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and g_board[nx][ny] > g_board[x][y] + 1:
                g_board[nx][ny] = g_board[x][y] + 1
                q.append((nx, ny))

def bfs(x, y, visit):
    q = deque()
    q.append((x, y))
    visit[x][y] = 0
    while q:
        x, y = q.popleft()
        if board[x][y] == 'D':
            print("Yes")
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 10000 and board[nx][ny] != '#' and g_board[nx][ny] > visit[x][y] + 1:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
    print("No")
    return

n, m = map(int, stdin.readline().split())
g_board = [[10000] * m for _ in range(n)]
visit = [[10000] * m for _ in range(n)]
board = [list(stdin.readline().strip()) for _ in range(n)]
s_x = s_y = 0
g_start_positions = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 'G':
            g_start_positions.append((i, j))
        elif board[i][j] == 'N':
            s_x = i
            s_y = j

g_bfs(g_start_positions, g_board)
bfs(s_x, s_y, visit)