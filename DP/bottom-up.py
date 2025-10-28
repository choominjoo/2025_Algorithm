#시간복잡도 O(n)
#공간복잡도 O(n)
def f(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(f(6))
# print(f(60)) 여기서는 실행됨