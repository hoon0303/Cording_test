from collections import deque

def solution(n, edge):
    answer = 0
    q = deque()
    
    dis = [-1]*(n+1)
    graph =[[] for _ in range(n+1)]
    
    for e in edge :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0]) 
        
    q.append(1)
    dis[1]=1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dis[i] == -1:
                dis[i] = dis[now]+1
                q.append(i)
    
    print(max(dis))

    for i in range(1, len(dis)):
        if dis[i] == max(dis):
            answer = answer + 1
    print(dis)
    return answer