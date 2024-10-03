import sys
sys.setrecursionlimit(10**6)

Test_case = int(input())
for T in range(Test_case):
    answer = 0
    M, N, K = map(int, input().split())
    board = [[0] * N for _ in range(M)]

    for k in range(K):
        x,y = map(int, input().split())

        board[x][y] = 1
    
    def dfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        board[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    dfs(nx, ny)

    for i in range(M):
        for j in range(N):
            if board[i][j] == 1:
                dfs(i,j)
                answer += 1
    print(answer)

