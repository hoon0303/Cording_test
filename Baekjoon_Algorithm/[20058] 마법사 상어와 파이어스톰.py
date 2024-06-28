import copy
from collections import deque

N, Q = map(int, input().split())
n = 2**N
board = [list(map(int,input().split())) for _ in range(n)]
new_board = [[0] * n for _ in range(n)]
L_list = list(map(int,input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def rotate(L):

    L = 2**L

    for x in range(0,n,L):
        for y in range(0,n,L):
            for i in range(L):
                for j in range(L):
                    new_board[x+j][y+L-i-1] = board[x+i][y+j]

    ice_board = copy.deepcopy(new_board)
    for x in range(n):
        for y in range(n):
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >=n or ny >= n or new_board[nx][ny] == 0:
                    continue
                else:
                    cnt = cnt + 1
            if cnt < 3 and new_board[x][y] != 0:
                ice_board[x][y] = new_board[x][y] - 1

    return ice_board

for L in L_list:
    board = rotate(L)


def check_ice_bfs(board, len_board):

    used = [[False] * len_board for _ in range(len_board)]
    ice_sum = 0 # 얼음 합
    max_area_count = 0 # 영역 크기
    for y in range(len_board):
        for x in range(len_board):
            area_count = 0
            if used[y][x] or board[y][x] == 0:
                continue
            # BFS를 이용하여 얼음 덩어리 조사
            q = deque()
            q.append((y, x))
            used[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx] # 얼음 합 추가
                area_count += 1  # 얼음 카운트 추가

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board or used[ny][nx]:
                        continue
                    if board[ny][nx] != 0:
                        used[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count) # 최대 얼음 덩어리 크기 파악

    print(ice_sum)
    print(max_area_count)

check_ice_bfs(board,n)