#분수 배낭 문제
#T(n) = nlogn + n = O(nlogn)
def ft(Name, Profit, Weight, C):
    L = list(zip(Name, Profit, Weight))
    S, maxP = [], 0
    L.sort(key = lambda k: k[1]/k[2], reverse = True)
    for n, p, w in L:
        if w > C:
            S.append((n, C/w))
            maxP += C*p/w
            break
        S.append((n, 1))
        C -= w
        maxP += p
    return maxP, S

Name = ['A', 'B', 'C']
Profit = [150, 100, 150]
Weight = [10, 20, 5]
Capacity = 20
print(ft(Name, Profit, Weight, Capacity))