from collections import deque

def bfs(x, graph, n):
    q = deque()
    q.append(x)
    visited = [False] * (n + 1)
    cnt = 0
    visited[x] = True
    while q:
        current = q.popleft()
        cnt += 1
        for v in graph[current]:
            if visited[v]:
                continue
            visited[v] = True
            q.append(v)

    return cnt

def solution(n, wires):
    answer = float('inf')

    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if i == j:
                continue
            graph[wires[j][0]].append(wires[j][1])
            graph[wires[j][1]].append(wires[j][0])
        cnt1 = bfs(1, graph, n)
        cnt2 = n - cnt1
        rst = cnt1-cnt2
        if rst < 0:
            rst = rst * -1
        answer = min(answer, rst)
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
solution(n, wires)
