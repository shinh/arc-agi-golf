def p(g):
    # find tile period
    for k in range(1,19):
        t=[[0]*k for _ in [0]*k]
        for y in range(18):
            for x in range(18):
                v=g[y][x]
                if v:
                    a=t[y%k][x%k]
                    if a and a!=v:break
                    t[y%k][x%k]=v
            else:continue
            break
        else:return[[t[y%k][x%k]for x in range(18)]for y in range(18)]
