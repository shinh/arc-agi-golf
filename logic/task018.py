def p(g):
    h=len(g);w=len(g[0])
    R=[*map(list,g)];S=set();T=[];r=range
    def F(i,j):
        if not(0<=i<h and 0<=j<w)or g[i][j]<1 or(i,j)in S:return[]
        S.add((i,j))
        return[(i,j)]+F(i+1,j)+F(i-1,j)+F(i,j+1)+F(i,j-1)
    for i in r(h):
        for j in r(w):
            if g[i][j]and(i,j)not in S:
                c=F(i,j)
                if len({g[x][y]for x,y in c})==4:
                    T.append(c)
                    for x,y in c:R[x][y]=0
    for c in T:
        xs,ys=zip(*c);mi,mj=min(xs),min(ys);H=max(xs)-mi+1;W=max(ys)-mj+1;cnt={};P=[[0]*W for _ in r(H)]
        for x,y in c:v=g[x][y];cnt[v]=cnt.get(v,0)+1;P[x-mi][y-mj]=v
        m=max(cnt,key=cnt.get)
        for t in P,[r[::-1]for r in P]:
            for _ in r(4):
                h2,w2=len(t),len(t[0])
                for i in r(h-h2+1):
                    for j in r(w-w2+1):
                        if all((u:=t[a][b])in(0,m)or R[i+a][j+b]==u for a in r(h2)for b in r(w2)):
                            for a in r(h2):
                                for b in r(w2):
                                    if(u:=t[a][b]):R[i+a][j+b]=u
                t=[*zip(*t[::-1])]
    return R
