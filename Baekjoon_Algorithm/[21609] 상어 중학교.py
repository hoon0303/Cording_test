import copy
from collections import deque

N, M = map(int,input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def find():
    m = []
    plt = 0
    visit = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            
            if visit[i][j] == 1000 or board[i][j] == 0 or board[i][j] == -1:
                continue
            check = copy.deepcopy(board)
            q = deque()
            q.append((i,j))

            check[i][j] = 1000
            visit[i][j] = 1000
            size = 1
            blank = 0
            while q:
                x,y = q.popleft()

                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y

                    if nx < 0 or ny < 0 or nx >=N or ny >= N or check[nx][ny] == 1000:
                        continue

                    if board[nx][ny] == board[i][j] or board[nx][ny] == 0:
                        check[nx][ny] = 1000
                        if board[nx][ny] != 0:
                            visit[nx][ny] = 1000
                        else:
                            blank = blank + 1
                        q.append((nx,ny))
                        size = size + 1
            
            if size >= 2:
                plt = plt + 1
                m.append([check, size, blank, i, j])
    if plt == 0:
        return board, 0

    m.sort(key=lambda x : (-x[1], -x[2],-x[3], -x[4]))
    return m[0][0], m[0][1]**2
def down():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1000:
                pos = i
                while True:
                    nx = pos - 1
                    if nx < 0:
                        break
                    if board[nx][j] == -1:
                        break
                    board[pos][j] = board[nx][j]
                    board[nx][j] = 1000
                    pos = nx
def rotate():
    newboard = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            newboard[N-j-1][i] = board[i][j]
    return newboard

result = 0
while True:
    x, rst = find()
    if rst == 0:
        break
    board = copy.deepcopy(x)
    result = result + rst

    down()

    x = rotate()
    board = copy.deepcopy(x)

    down()

print(result)