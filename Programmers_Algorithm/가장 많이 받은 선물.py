from itertools import combinations
gisu = dict()
gifted = dict()
rst = dict()
def solution(friends, gifts):
    answer = 0
    
    for friend in friends:
        gisu[friend] = 0
        gifted[friend] = {}
        rst[friend] = 0
    
            
    for gift in gifts:
        give, take = gift.split(' ')
        if take in gifted[give]:
            gifted[give][take] += 1
        else:
            gifted[give][take] = 1
        gisu[give] += 1
        gisu[take] -= 1
    
    x = combinations(friends,2)

    for i in x:
        x1,x2 = i
        
        a=0
        b=0
        if x2 in gifted[x1]:
            a= gifted[x1][x2]
        if x1 in gifted[x2]:
            b= gifted[x2][x1]
        
        if a> b:
            rst[x1] += 1
        elif b > a:
            rst[x2] += 1
        else:
            if gisu[x1] > gisu[x2]:
                rst[x1] += 1
            elif gisu[x1] < gisu[x2]:
                rst[x2] += 1
    
    rst2=sorted(rst.items(), key=lambda x: -x[1])

    answer = rst2[0][1]
    return answer