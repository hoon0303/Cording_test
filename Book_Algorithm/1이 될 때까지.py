def solution(N,K):
    rst = 0

    while(N > 1):
        if N % K ==0:
            N = N//K
        else:
            N -= 1
        rst+=1
    return rst

N,K = map(int, input().split())
rst = solution(N,K)
print(rst)