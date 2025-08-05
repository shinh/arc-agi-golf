def p(g):
    n=w=16;o=[r[:] for r in g]
    for i in range(n//2):
        j=n-1-i;r1=g[i];r2=g[j]
        if r1==r1[::-1]:o[i]=o[j]=r1
        elif r2==r2[::-1]:o[i]=o[j]=r2
        else:s=r1[:w//2];o[i]=o[j]=s+s[::-1]
    return o
