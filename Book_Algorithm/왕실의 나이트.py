
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]


def solution(x):
    row = int(x[1])
    column = int(ord(x[0])) - int(ord('a')) + 1
    cnt = 0
    for i in range(8):
        nx = row + dx[i]
        ny = column + dy[i]

        if nx < 1 or ny < 1 or nx > 8 or ny >8:
            continue
        cnt += 1
    return cnt
x = input()
rst = solution(x)
print(rst)

