

def dfs(ans, n, m, i, total):
    if i > m:
        return 0
    if total > n:
        return 0
    if total == n:
        return 1
    total += i
    ans += dfs(ans, n, m, i, total)
    total -= i
    ans += dfs(ans, n, m, i + 1, total)
    return ans

print(counting_partition(6, 4))