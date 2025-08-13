# 375
def p(g):
    bg=max(g[0],key=g[0].count)
    m=[]
    L=0
    for c in range(10):
        mx=0,
        for t in[g,zip(*g)]:
            for r in t:
                if c in r:
                    l=r[r.index(c):len(r)-r[::-1].index(c)]
                    q=n=len(l)
                    if set(l)!={c}:
                        n1=n2=0
                        while l[0]==c:
                            l=l[1:]
                            n1+=1
                        while l[-1]==c:
                            l=l[:-1]
                            n2+=1
                        q=max(n1,n2)
                        n=q*2+len(l)
                    mx=max(mx,(n,q))
        if mx[0] and c!=bg:
            m+=[c,*mx],
            L=max(L,mx[0])
    o=[[bg]*L for _ in range(L)]
    for c,n,q in m:
        if n==2:n=3
        for _ in range(4):
            for i in range(q):
                o[(L-n)//2][(L-n)//2+i]=o[(L-n)//2+i][(L-n)//2]=c
            o=[*map(list,zip(*o[::-1]))]
    return o
