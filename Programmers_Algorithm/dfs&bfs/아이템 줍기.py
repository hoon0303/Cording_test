from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    board = [[-1]*201 for _ in range(201)]
    
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rect)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1 < i <x2 and y1 < j < y2:
                    board[i][j] = 0
                elif board[i][j] != 0:
                    board[i][j] = 1

    def bfs(x,y):
        q = deque()
        cnt = 0
        q.append([x*2,y*2, cnt])
        
        while q:
            x,y, cnt = q.popleft()
            if x == itemX*2 and y == itemY*2:
                return cnt//2
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx > 200 or ny > 200:
                    continue
                if board[nx][ny] == 1:
                    board[nx][ny] = 2
                    q.append([nx, ny ,cnt + 1])
    answer = bfs(characterX,characterY)
    return answer
