def solution(citations):
    answer = 0
    
    citations.sort()
    n = len(citations)
    
    for i in range(n):
        h_index = n-i
        
        if citations[i] >= h_index:
            answer = h_index
            break
        
    return answer

citations = [3, 0, 6, 1, 5]

print(solution(citations))