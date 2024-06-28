check = [0] * 201

def dfs(i, computers):
    if check[i] == 1:
        return 0
    print(len(computers[i]))
    check[i] = 1
    for j in range(len(computers[i])):
        if computers[i][j] == 1:
            dfs(j, computers)

    return 1
    
def solution(n, computers):
    answer = 0
    
    print(computers)
    
    for i in range(len(computers[0])):
        
        answer = answer + dfs(i, computers)
    return answer