def p(g):
    h=len(g);w=len(g[0]);s=set();o=[];d=[0]*10
    for y in range(h):
        for x in range(w):
            if g[y][x]<1 or(y,x)in s:continue
            q=[(y,x)];s.add((y,x));c=[]
            while q:
                i,j=q.pop();c+=[(i,j)]
                for dy in(-1,0,1):
                    for dx in(-1,0,1):
                        ni=i+dy;nj=j+dx
                        if dy|dx and 0<=ni<h and 0<=nj<w and g[ni][nj]and(ni,nj)not in s:
                            q+=[(ni,nj)];s.add((ni,nj))
            for a in{g[i][j]for i,j in c}:d[a]+=1
            o+=[c]
    k=d.index(max(d));t=min(o,key=lambda e:(sum(g[i][j]==k for i,j in e),-len(e)));o.remove(t)
    ti,tj=map(min,zip(*t))
    t=[(i-ti,j-tj,g[i][j]==k)for i,j in t];y,x=min((i,j)for i,j,v in t if v)
    r=[r[:]for r in g]
    for e in o:
        ys,xs=zip(*[(i,j)for i,j in e if g[i][j]==k])
        Y=min(ys);X=min(xs);n=max(xs)+1-X
        oc=next(v for i,j in e if(v:=g[i][j])!=k)
        for i,j,v in t:
            for a in range(n*n):
                ii=i*n+a//n+Y-y*n;jj=j*n+a%n+X-x*n
                if 0<=ii<h and 0<=jj<w:r[ii][jj]=[oc,k][v]
    return r
