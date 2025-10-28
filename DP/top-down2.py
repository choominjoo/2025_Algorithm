#시간복잡도 O(n)
#공간복잡도 O(n)
def f(n):
    if memo[n] >= 0:
        return memo[n]
    if n < 2:
        memo[n] = n
    else:
        memo[n] = f(n - 1) + f(n - 2)
    return memo[n]

n = 6
memo = [-1] * (n + 1)   #리스트 저장소
print(f(n))   #8
print(memo)   #[0, 1, 1, 2, 3, 5, 8]

n = 60
memo = [-1] * (n + 1)   #리스트 저장소
print(f(n))   #1548008755920