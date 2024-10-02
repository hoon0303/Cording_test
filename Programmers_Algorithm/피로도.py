from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # 모든 던전 순열을 확인
    for perm in permutations(dungeons):
        current_k = k
        cnt = 0
        
        # 던전 순서대로 탐험 시도
        for dungeon in perm:
            if current_k >= dungeon[0]:  # 최소 필요 피로도 확인
                current_k -= dungeon[1]  # 소모 피로도만큼 감소
                cnt += 1  # 던전 하나 탐험 성공
            else:
                break  # 피로도가 부족하면 더 이상 탐험 불가능
        
        # 최대 던전 수 갱신
        answer = max(answer, cnt)
    
    return answer
