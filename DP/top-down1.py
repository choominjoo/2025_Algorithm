#시간복잡도 O(n)
#공간복잡도 O(n)
def f(n):
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = n
    else:
        memo[n] = f(n - 1) + f(n - 2)
    return memo[n]

memo = {}   #사전 저장소
print(f(6))   #8
print(memo)   #{1: 1, 0: 0, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8}

memo = {}   #사전 저장소
print(f(60))   #1548008755920