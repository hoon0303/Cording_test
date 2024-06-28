from collections import deque
N, M = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
board = []

for i in range(N):
    board.append(list(map(str, input().rstrip())))

def getpos():
    Rnx = 0
    Rny = 0
    Bnx = 0
    Bny = 0
    for i in range(0,N-1):
        for j in range(0,M-1):
            if board[i][j] == "R":
                Rnx = i
                Rny = j
            if board[i][j] == "B":
                Bnx = i
                Bny = j
    return Bnx, Bny, Rnx, Rny

def move(x, y, dx, dy):
    cnt = 0
    # 이동하는 위치가 벽이아니고, 구멍에 들어가지 않을 동안 반복
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        cnt +=1
    return x, y, cnt

def bfs():
    rx, ry, bx, by = getpos()
    visit = []
    q = deque()
    q.append((rx, ry, bx, by,1))
    visit.append((rx, ry, bx, by))



    while q:
        Bnx, Bny, Rnx, Rny, cnt = q.popleft()

        if cnt > 10:
            print(-1)
            return
        for i in range(4):
            nbx, nby, Bcnt = move(Bnx, Bny, dx[i], dy[i])
            nrx, nry, Rcnt = move(Rnx, Rny, dx[i], dy[i])
            if board[nbx][nby] == "O":
                continue

            if board[nrx][nry] == "O":
                print(cnt)
                return

            # 둘이 겹쳐있을경우 더 많이 이동한녀석을 1칸 뒤로 보낸다.
            if nrx == nbx and nby == nry:
                if Rcnt > Bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nbx, nby, nrx, nry) not in visit:
                q.append((nbx, nby, nrx, nry, cnt + 1))
                visit.append((nbx, nby, nrx, nry))
                #print(nbx, nby, nrx, nry)
    print(-1)

bfs()