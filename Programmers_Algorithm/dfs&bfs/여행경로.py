def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    data = dict()
    for ticket in tickets:
        if ticket[0] not in data:
            data[ticket[0]] = list()
            
        data[ticket[0]].append(ticket[1])
    
    stack = ['ICN']
    
    while stack:
        top = stack[-1]
        
        if top in data and data[top]:
            stack.append(data[top].pop())
        else:
            answer.append(stack.pop())
    
    return answer[::-1]
