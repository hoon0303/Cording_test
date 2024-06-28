def solution(clothes):
    answer = 1
    
    temp = dict()
    for cloth in clothes:
        try:
            temp[cloth[1]] = temp[cloth[1]] + 1
        except:
            temp[cloth[1]] = 1
            
    for i in temp:
        answer = answer * (temp[i] + 1)
        
    return answer - 1