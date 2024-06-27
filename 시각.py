def solution(N):
    rst = 0
    for i in range(N+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    rst += 1
    print(rst)
N = int(input())
solution(N)