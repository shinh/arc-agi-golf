def p(g):
    h=15;w=10;R=range
    P=[];pr=-9
    for i,r in enumerate(g):
        if 8 in r:P+=[set()]*(i-pr>1);P[-1]|={(i,j)for j,v in enumerate(r)if v==8};pr=i
    if not P:return g
    T=max(P,key=lambda p:max(j for _,j in p)-min(j for _,j in p));P.remove(T)
    a=min(i for i,_ in T);b0=min(j for _,j in T)
    T=[(i-a,j-b0)for i,j in T]
    for p in P:
        b=(-1,0,0);rm=max(j for _,j in p);best=set()
        for dx in R(-h,h):
            for dy in R(-w,w+w):
                S={(i+dx,j+dy)for i,j in T if -1<i+dx<h and -1<j+dy<w}
                D=S-p
                if D and min(j for _,j in D)>rm:
                    t=len(p&S),dy,dx
                    if t>b:b=t;best=D
        for i,j in best:g[i][j]=1
    return g
