
def solution(n, money):
    rst = 0
    money.sort(reverse = True)

    for coin in money:
        rst += (n // coin)
        n %= coin
    return rst

n = 1260
money = [500,100,50,10]

rst = solution(n, money)
print(rst)