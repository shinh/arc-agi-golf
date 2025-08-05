def p(g):
    h=len(g);w=len(g[0])
    R=[*map(list,g)];S=set();r=range
    def F(i,j):
        if not(0<=i<h and 0<=j<w)or g[i][j]<1 or(i,j)in S:return[]
        S.add((i,j));s.add(g[i][j])
        return[(i,j)]+F(i+1,j)+F(i-1,j)+F(i,j+1)+F(i,j-1)
    for i in r(h):
        for j in r(w):
            if g[i][j]and(i,j)not in S:
                s=set();c=F(i,j)
                if len(s)==4:
                    for x,y in c:R[x][y]=0
                    xs,ys=zip(*c);mi,mx=min(xs),max(xs);mj,my=min(ys),max(ys);P=[[0]*(my-mj+1)for _ in r(mx-mi+1)];C={}
                    for x,y in c:u=g[x][y];C[u]=C.get(u,0)+1;P[x-mi][y-mj]=u
                    m=max(C,key=C.get)
                    for t in P,P[::-1]:
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
