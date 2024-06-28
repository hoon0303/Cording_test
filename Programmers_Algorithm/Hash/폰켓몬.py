def solution(nums):
    answer = 0
    s = set(nums)
    l = len(nums)/2
    
    if l > len(s):
        return len(s)
    answer = l
    
    return int(answer)

nums = [3,1,2,3]

print(solution(nums))