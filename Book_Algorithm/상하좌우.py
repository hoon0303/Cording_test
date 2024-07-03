
def solution(N, arr):

    d = dict()
    d['L'] = [0,-1]
    d['R'] = [0,1]
    d['U'] = [-1,0]
    d['D'] = [1,0]
    x = 1
    y = 1
    for a in arr:
        move_x, move_y = d[a]
        nx = x + move_x
        ny = y + move_y

        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue
        x = nx
        y = ny

    print(x, y)
    return

N = int(input())
arr = map(str, input().split())

solution(N, arr)