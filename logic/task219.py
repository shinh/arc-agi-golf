def p(g):
    h=15;w=10;R=range
    rows=[i for i,r in enumerate(g) if 8 in r]
    if not rows:return [r[:]for r in g]
    B=[];b=[rows[0]]
    for i in rows[1:]:
        if i==b[-1]+1:b.append(i)
        else:B.append(b);b=[i]
    B.append(b)
    P=[{(i,j)for i in b for j,v in enumerate(g[i])if v==8} for b in B]
    wdt=lambda p:max(j for _,j in p)-min(j for _,j in p)
    T=max(P,key=wdt);P.remove(T)
    a=min(i for i,_ in T);b0=min(j for _,j in T)
    T=[(i-a,j-b0)for i,j in T]
    add=set()
    for p in P:
        sc=-1;bd=bx=0;rm=max(j for _,j in p)
        for dx in R(-h,h+1):
            for dy in R(-w,w*2):
                S={(i+dx,j+dy)for i,j in T};k=len(p&S)
                D={q for q in S-p if 0<=q[0]<h and 0<=q[1]<w}
                if not D or min(j for _,j in D)<=rm:continue
                if k>sc or (k==sc and dy>bd) or (k==sc and dy==bd and dx>bx):
                    sc=k;best=D;bd=dy;bx=dx
        add|=best
    r=[row[:]for row in g]
    for i,j in add:
        if 0<=i<h and 0<=j<w:r[i][j]=1
    return r
