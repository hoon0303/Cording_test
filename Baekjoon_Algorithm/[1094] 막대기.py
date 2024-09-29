x = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(stick)):
    if x >= stick[i]:
        count += 1
        x -= stick[i]

    if x == 0:
        break

print(count)
