

n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = [list(map(int, input().split())) for _ in range(m)]

total = 0
arr = [0]
for i in range(n):
    total = arr1[i] + total
    arr.append(total)

print(arr)

for a in arr2:
    print(arr[a[1]]- arr[a[0]-1])