def p(g):
    h=len(g);w=len(g[0])
    bg=max(range(10),key=lambda c:sum(r.count(c)for r in g))
    seen=set();objs=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]!=bg and(i,j)not in seen:
                q=[(i,j)];cells=[];seen.add((i,j))
                while q:
                    x,y=q.pop();cells.append((x,y,g[x][y]))
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        X,Y=x+dx,y+dy
                        if 0<=X<h and 0<=Y<w and g[X][Y]!=bg and(X,Y)not in seen:
                            seen.add((X,Y));q.append((X,Y))
                objs.append(cells)
    res=[r[:]for r in g];targets=[]
    for c in objs:
        if len({v for _,_,v in c})==4:
            targets.append(c)
            for i,j,_ in c:res[i][j]=bg
    for c in targets:
        mi=min(i for i,_,_ in c);mj=min(j for _,j,_ in c)
        mx=max(i for i,_,_ in c);my=max(j for _,j,_ in c)
        P=[[bg]*(my-mj+1)for _ in range(mx-mi+1)]
        cnt={}
        for i,j,v in c:cnt[v]=cnt.get(v,0)+1;P[i-mi][j-mj]=v
        maj=max(cnt,key=cnt.get)
        for f in 0,1:
            T=[row[::-1]for row in P]if f else[row[:]for row in P]
            for _ in 0,1,2,3:
                h2=len(T);w2=len(T[0])
                core=[(a,b,T[a][b])for a in range(h2)for b in range(w2)if T[a][b]!=maj and T[a][b]!=bg]
                for i in range(h-h2+1):
                    for j in range(w-w2+1):
                        if all(res[i+a][j+b]==v for a,b,v in core):
                            for a in range(h2):
                                R=res[i+a];Pa=T[a]
                                for b in range(w2):
                                    v=Pa[b]
                                    if v!=bg:R[j+b]=v
                T=[list(x)for x in zip(*T)][::-1]
    return res
