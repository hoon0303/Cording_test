from collections import deque
import copy
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [-1,1,0,0]
rst = 0

def dfs(x,y,cnt,sum,visit):
    global rst, w

    if cnt == 4:

        rst = max(sum, rst)
        return
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if nx <0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visit[nx][ny] == 1 :
            continue
        v= copy.deepcopy(visit)
        v[nx][ny] = 1
        dfs(nx,ny,cnt+1,sum + board[nx][ny],v)

def exce(i, j):
    global rst
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = i+dx[t]
            nj = j+dy[t]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        rst = max(rst, tmp)


for i in range(N):
    for j in range(N):
        visit = [[0] * N for _ in range(N)]
        visit[i][j] = 1
        dfs(i,j,1,board[i][j], visit)
        exce(i,j)
print(rst)