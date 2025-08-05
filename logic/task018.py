def p(g):
    h=len(g);w=len(g[0])
    R=[r[:]for r in g];S=set();T=[]
    def F(i,j):
        if not(0<=i<h and 0<=j<w) or g[i][j]==0 or(i,j)in S:return[]
        S.add((i,j));v=g[i][j]
        return[(i,j,v)]+F(i+1,j)+F(i-1,j)+F(i,j+1)+F(i,j-1)
    for i in range(h):
        for j in range(w):
            if g[i][j] and(i,j)not in S:
                c=F(i,j)
                if len({v for _,_,v in c})==4:
                    T.append(c)
                    for x,y,_ in c:R[x][y]=0
    for c in T:
        mi=min(x for x,_,_ in c);mj=min(y for _,y,_ in c);mx=max(x for x,_,_ in c);my=max(y for _,y,_ in c)
        H=mx-mi+1;W=my-mj+1;cnt={};P=[[0]*W for _ in range(H)]
        for x,y,v in c:cnt[v]=cnt.get(v,0)+1;P[x-mi][y-mj]=v
        m=max(cnt,key=cnt.get)
        for t in(P,[r[::-1]for r in P]):
            for _ in 0,1,2,3:
                h2=len(t);w2=len(t[0])
                for i in range(h-h2+1):
                    for j in range(w-w2+1):
                        if all(R[i+a][j+b]==u for a in range(h2)for b in range(w2)if(u:=t[a][b])not in(0,m)):
                            for a in range(h2):
                                for b in range(w2):
                                    u=t[a][b]
                                    if u:R[i+a][j+b]=u
                t=[*zip(*t)][::-1]
    return R
