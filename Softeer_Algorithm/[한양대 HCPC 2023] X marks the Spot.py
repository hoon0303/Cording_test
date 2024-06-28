from sys import stdin

n = int(input())

rst = []
for i in range(n):
    a, b = map(str, stdin.readline().split())
    a = a.upper()
    idx = a.find('X')

    rst.append(b[idx].upper()) 

print(''.join(rst))