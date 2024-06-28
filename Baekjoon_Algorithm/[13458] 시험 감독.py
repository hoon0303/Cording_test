N = int(input())
Exam = list(map(int, input().split()))
B, C = map(int, input().split())

rst = 0

for i in Exam:
    x = i - B
    if x > 0:
        C__num = int(x//C)
        if x%C != 0:
            C__num = C__num + 1
        rst = rst + C__num

print(rst + N)