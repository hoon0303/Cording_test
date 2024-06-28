cnt = 0
def dfs(idx, sum, numbers, target):
    global cnt
    if idx >= len(numbers):
        if target == sum:
            cnt = cnt + 1
        return
    dfs(idx+1,sum+numbers[idx],numbers, target)
    dfs(idx+1,sum-numbers[idx],numbers, target)

def solution(numbers, target):
    answer = 0
    dfs(0,0,numbers,target)
    return cnt