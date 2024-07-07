
N = int(input())

list = dict()
dx = [0,0,-1,1]
dy = [1,-1,0,0]

board = [[0] * N for _ in range(N)]

for i in range(N*N):
    x, f1, f2, f3, f4 = map(int, input().split())
    list[x] = [f1,f2,f3,f4]

def find(student):
    pos = []
    for i in range(N):
        for j in range(N):
            
            if board[i][j] != 0:
                continue
            friend = 0
            blank = 0
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j

                if nx < 0 or ny < 0 or nx >=N or ny >= N:
                    continue
                if board[nx][ny] in list[student]:
                    friend = friend + 1
                if board[nx][ny] == 0:
                    blank = blank + 1
            pos.append([friend, blank , i, j])
    pos.sort(key=lambda x : (-x[0],-x[1], x[2],x[3]))
    board[pos[0][2]][pos[0][3]] = student
    
    
def score():
    rst = 0
    for i in range(N):
        for j in range(N):
            freind = 0
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if nx < 0 or ny < 0 or nx >=N or ny >= N:
                    continue
                if board[nx][ny] in list[board[i][j]]:
                    freind = freind + 1
            if freind ==2:
                rst = rst + 10
            elif freind ==3:
                rst = rst + 100
            elif freind == 4:
                rst = rst + 1000
            else:
                rst = rst + freind

    print(rst)

for x in list:
    find(x)

score()