def p(g):
    h=w=12;P={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):P.setdefault(v,[]).append((i,j))
    for k,v in P.items():
        S=set(v)
        if k and all((i+1,j)not in S and (i-1,j)not in S and (i,j+1)not in S and (i,j-1)not in S for i,j in S):
            a=k;A=S;break
    for v in P.values():
        r=[i for i,_ in v];c=[j for _,j in v]
        if len(v)==(max(r)-min(r)+1)*(max(c)-min(c)+1):R=min(r);B=max(r);C=min(c);D=max(c)
    r8=min(i for i,_ in A);c8=min(j for _,j in A)
    def d(i,j):return max(C-j,0,j-D)+max(R-i,0,i-B)
    t=min(A,key=lambda p:d(*p))
    e,f=((1,1),(-1,-1))if(r8,c8)in A else((1,-1),(-1,1))
    if d(t[0]+e[0],t[1]+e[1])>d(t[0]+f[0],t[1]+f[1]):e=f
    i,j=t
    while not((R-1<=i<=B+1 and j in (C-1,D+1)) or (C-1<=j<=D+1 and i in (R-1,B+1))):i+=e[0];j+=e[1]
    if B-R+1==h:dirs=[(1,1),(-1,1)]if c8>C else[(1,-1),(-1,-1)]
    else:dirs=[(1,1),(1,-1)]if r8>R else[(-1,-1),(-1,1)]
    for di,dj in dirs:
        x,y=i,j
        while 0<=x<h and 0<=y<w:
            if g[x][y]!=a:g[x][y]=3
            x+=di;y+=dj
    return g
