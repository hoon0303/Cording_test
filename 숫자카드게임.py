
def solution(arr):
    rst = 0
    for a in arr:
        rst = max(rst, min(a))
    return rst

N, M = map(int, input().split())
arr = [map(int, input().split()) for _ in range(N)]

rst = solution(arr)
print(rst)