def p(g):
    h=len(g);w=len(g[0]);H=3*h;W=3*w
    b=max(range(10),key=lambda c:sum(r.count(c)for r in g))
    B=[[b]*W for _ in range(H)]
    for i in range(h):
        for j in range(w):B[h+i][w+j]=g[i][j]
    D=(-1,0,1);vis=set();objs=[]
    for i in range(H):
        for j in range(W):
            if B[i][j]!=b and(i,j)not in vis:
                q=[(i,j)];vis.add((i,j));s=set();col={}
                while q:
                    y,x=q.pop();s.add((y,x));v=B[y][x];col[v]=col.get(v,0)+1
                    for dy in D:
                        for dx in D:
                            if dy or dx:
                                Y,X=y+dy,x+dx
                                if 0<=Y<H and 0<=X<W and B[Y][X]!=b and(Y,X)not in vis:
                                    vis.add((Y,X));q.append((Y,X))
                objs.append((s,col))
    tm=max(objs,key=lambda o:len(o[1]))
    objs.remove(tm)
    cnt={}
    for _,c in objs:
        for k,v in c.items():cnt[k]=cnt.get(k,0)+v
    m=max(cnt,key=cnt.get)
    s,c=tm
    mi=min(i for i,_ in s);mj=min(j for _,j in s)
    T=[(i-mi,j-mj,B[i][j]) for i,j in s]
    A=[(i,j)for i,j,v in T if v==m];Z=[(i,j)for i,j,v in T if v!=m]
    th=max(i for i,_,_ in T)+1;tw=max(j for _,j,_ in T)+1
    C=[]
    for k in range(1,6):
        for y in range(H-th*k+1):
            for x in range(W-tw*k+1):
                ok=1;S=set()
                for i,j in A:
                    for dy in range(k):
                        for dx in range(k):
                            Y=y+i*k+dy;X=x+j*k+dx
                            if B[Y][X]!=m:ok=0;break
                            S.add((Y,X))
                        if not ok:break
                    if not ok:break
                if not ok:continue
                for i,j in Z:
                    for dy in range(k):
                        for dx in range(k):
                            if B[y+i*k+dy][x+j*k+dx]!=b:ok=0;break
                        if not ok:break
                    if not ok:break
                if not ok:continue
                U=set()
                for s2,_ in objs:
                    if s2&S:U|=s2
                if len(U)==len(S):C.append((y,x,k))
    for y,x,k in C:
        for i,j,v in T:
            for dy in range(k):
                for dx in range(k):
                    B[y+i*k+dy][x+j*k+dx]=v
    return [r[w:2*w]for r in B[h:2*h]]
