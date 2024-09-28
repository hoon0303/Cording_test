def solution(diffs, times, limit):
    answer = 0
    
    left = min(diffs)
    right = max(diffs)
    mid = 0
    
    while left <= right:
        mid = int((right + left)/2)
        total_time = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                total_time += times[i]
            else:
                total_time += ((diffs[i] - mid) * (times[i-1] + times[i]) + times[i])
        #print(total_time,mid)
        if total_time <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
