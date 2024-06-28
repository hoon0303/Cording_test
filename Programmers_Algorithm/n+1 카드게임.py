from collections import deque

def find(X,Y,N):
    for x in X:
        if N-x in Y:
            X.remove(x)
            Y.remove(N-x)
            print(x, N-x)
            return 1
    return 0

def solution(coin, cards):
    answer = 0
    N = len(cards) + 1
    
    card = cards[:N//3]
    q = deque(cards[N//3:])
    pos = list()
    
    while q:
        a = q.popleft()
        b = q.popleft()
        pos.append(a)
        pos.append(b)
        
        if find(card, card, N):
            answer = answer + 1
        elif find(card, pos,N) and coin >= 1:
            coin = coin - 1
            answer = answer + 1
        elif find(pos, pos,N) and coin >= 2:
            coin = coin - 2
            answer = answer + 1
        else:
            break
    return answer + 1