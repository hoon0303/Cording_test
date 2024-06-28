def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3,reverse=True)
    
    for i in numbers:
        #answer += i
        answer = answer + i
    
    answer = str(int(answer))
    return answer

numbers = [6, 10, 2]

print(solution(numbers))