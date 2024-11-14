from itertools import permutations, product

N,M = map(int, input().split())
board = [i+1 for i in range(N)]

ans = list(product(board,repeat=M))

for a in ans:
    for i in a:
        print(i, end=' ')
    print()
