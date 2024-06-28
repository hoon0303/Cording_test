

N = int(input())

work = [list(map(int,input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + work[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], work[i][1] + dp[i + work[i][0]])
print(dp)
