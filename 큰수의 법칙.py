

def solution(N,M,K,numbers):
    rst = 0
    numbers.sort(reverse = True)
    
    cnt = M//(K+1) * K
    cnt += M%(K+1)

    rst += numbers[0] * cnt
    rst += numbers[1] * (M-cnt)
    return rst

input1 = "5 8 3"
input2 = "2 4 5 4 6"
N, M, K = map(int, str.split(input1))
numbers = list(map(int, str.split(input2)))

rst = solution(N,M,K,numbers)
print(rst)