import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dijkastra():
    q = []
    heapq.heappush(q, (board[0][0], 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)

        if x == N-1 and y  == N-1:
            print(f"Problem {cnt}: {distance[x][y]}")
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            n_cost = cost + board[nx][ny]
            if distance[nx][ny] > n_cost:
                distance[nx][ny] = n_cost
                heapq.heappush(q, (n_cost, nx,ny))

cnt = 1
while(True):
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    dijkastra()
    cnt += 1