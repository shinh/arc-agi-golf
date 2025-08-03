def p(g):
    n=len(g)
    for k in range(1,n+1):
        t=[[-1]*k for _ in range(k)]
        for y in range(n):
            for x in range(n):
                v=g[y][x]
                if v:
                    a=t[y%k][x%k]
                    if a<0:t[y%k][x%k]=v
                    elif a!=v:break
            else:continue
            break
        else:return[[t[y%k][x%k]for x in range(n)]for y in range(n)]
