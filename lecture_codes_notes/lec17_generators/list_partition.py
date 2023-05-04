def list_partition(n, m):
        if m == 0:
            return []
        if n < m:
            return list_partition(n,n)
        else:
            match = []
            if n == m:
                match = [[m]]
                return match + list_partition(n, m-1)
            with_m = [[m] + p for p in list_partition(n-m, m)]
            without_m = list_partition(n, m-1)
            return with_m + without_m



for p in list_partition(6, 4):
    print(p)