def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)

print(f(5))
# print(f(60))