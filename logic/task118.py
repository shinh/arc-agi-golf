def p(g):
    H=len(g);W=len(g[0])
    C=min({v for r in g for v in r},key=lambda k:sum(r.count(k)for r in g))
    O={(i,j)for i in range(H)for j in range(W)if g[i][j]==C}
    S=set(O);f=1
    while f:
        f=0
        for i in range(H):
            xs=[j for j in range(W)if(i,j)in S]
            for a,b in zip(xs,xs[1:]):
                if b-a<5:
                    for k in range(a+1,b):
                        if(i,k)not in S:S.add((i,k));f=1
        for j in range(W):
            ys=[i for i in range(H)if(i,j)in S]
            for a,b in zip(ys,ys[1:]):
                if b-a<5:
                    for k in range(a+1,b):
                        if(k,j)not in S:S.add((k,j));f=1
    T={(i,j)for i,j in S if((i,j-1)in S or(i,j+1)in S)and((i-1,j)in S or(i+1,j)in S)}
    R=set(S);I=[];L=0
    while R:
        st=[R.pop()];comp=[]
        while st:
            i,j=st.pop();comp.append((i,j))
            for di in(-1,0,1):
                for dj in(-1,0,1):
                    if di or dj:
                        n=(i+di,j+dj)
                        if n in R:R.remove(n);st.append(n)
        ys=[i for i,_ in comp];xs=[j for _,j in comp]
        h=max(ys)-min(ys)+1;w=max(xs)-min(xs)+1;d=max(h,w);L=max(L,d)
        I.append((comp,min(ys),min(xs),h,w,d))
    for comp,y,x,h,w,d in I:
        if d==L and (h==1 or w==1):T.add((y+h//2,x+w//2))
    m=L//2
    for i,j in T:
        for d in range(-m,m+1):
            if 0<=i+d<H:S.add((i+d,j))
            if 0<=j+d<W:S.add((i,j+d))
    r=[r[:]for r in g]
    for i,j in S:r[i][j]=8
    for i,j in O:r[i][j]=C
    return r

# Failed attempt:
# def p(g):
#     H=len(g);W=len(g[0])
#     for l in range(2,6):
#         seen={}
#         for y in range(H):
#             for x in range(W):
#                 if (x,y)in seen:continue
#                 ok=1
#                 for i in range(-l,l+1):
#                     if x+i>=0 and x+i<W and g[y][x+i]==0:
#                         ok=0
#                     if y+i>=0 and y+i<H and g[y+i][x]==0:
#                         ok=0
#                 if ok:
#                     seen[(x,y)]=1
#                     for i in range(-l,l+1):
#                         if x+i>=0 and x+i<W:
#                             g[y][x+i]=8
#                         if y+i>=0 and y+i<H:
#                             g[y+i][x]=8
#     show(g,"out")
#     return g
