def p(g):
    H,W=len(g),len(g[0]);f=[c for r in g for c in r];b=max(set(f),key=f.count)
    s=set();o=[];d=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(H):
        for j in range(W):
            if g[i][j]!=b and(i,j)not in s:
                q=[(i,j)];s.add((i,j));pts=[];pal=set()
                while q:
                    x,y=q.pop();pts.append((x,y));pal.add(g[x][y])
                    for dx,dy in d:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and g[nx][ny]!=b and(nx,ny)not in s:
                            s.add((nx,ny));q.append((nx,ny))
                o.append((pts,pal))
    p1,_=max(o,key=lambda x:len(x[1]));p2,_=min(o,key=lambda x:len(x[1]));c=g[p2[0][0]][p2[0][1]]
    xs=[x for x,_ in p2];ys=[y for _,y in p2];mi,ma=min(xs),max(xs);mj,mz=min(ys),max(ys)
    h2=ma-mi+1;w2=mz-mj+1;bg=[[b]*w2 for _ in range(h2)]
    for x,y in p2:bg[x-mi][y-mj]=g[x][y]
    xs1=[x for x,_ in p1];ys1=[y for _,y in p1];n1,miny=min(xs1),min(ys1)
    h1=max(xs1)-n1+1;w1=max(ys1)-miny+1;si=h2//h1;sj=w2//w1
    out=[[bg[i*si][j*sj] for j in range(w1)] for i in range(h1)]
    for x,y in p1:
        i=x-n1;j=y-miny
        if out[i][j]==c:out[i][j]=g[x][y]
    return out
