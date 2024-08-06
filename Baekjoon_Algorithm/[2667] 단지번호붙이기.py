from collections import deque

N = int(input())
board = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(board, x,y):
    n = len(board)
    cnt = 1
    q = deque()
    q.append((x,y))
    board[x][y] = 0
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt        

rst = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cnt = bfs(board, i,j)
            rst.append(cnt)

print(len(rst))
rst.sort()
for i in rst:
    print(i)
