def p(g):
    h=len(g);W=len(g[0]);v=set();o=[];d={}
    for y in range(h):
        for x in range(W):
            if g[y][x]<1 or(y,x)in v:continue
            q=[(y,x)];v.add((y,x));c=[];s=set()
            while q:
                i,j=q.pop();c+=[(i,j)];s.add(g[i][j])
                for dy in(-1,0,1):
                    for dx in(-1,0,1):
                        ni=i+dy;nj=j+dx
                        if dy|dx and 0<=ni<h and 0<=nj<W and g[ni][nj]and(ni,nj)not in v:
                            q+=[(ni,nj)];v.add((ni,nj))
            for a in s:d[a]=1+d.get(a,0)
            o+=[c]
    k=max(d,key=d.get);s=[sum(g[i][j]==k for i,j in x)for x in o]
    t=max([x for x,r in zip(o,s)if r==min(s)],key=len);o=[x for x in o if x!=t]
    ti=min(i for i,_ in t);tj=min(j for _,j in t)
    t=[(i-ti,j-tj,g[i][j]==k)for i,j in t];y,x=min((i,j)for i,j,v in t if v)
    r=[x[:]for x in g]
    for e in o:
        xs=[(i,j)for i,j in e if g[i][j]==k]
        Y=min(i for i,j in xs);X=min(j for i,j in xs);n=max(j for i,j in xs)-X+1
        oc=next(g[i][j] for i,j in e if g[i][j]!=k)
        for i,j,v in t:
            for a in range(n*n):
                ii=i*n+a//n+Y-y*n;jj=j*n+a%n+X-x*n
                if 0<=ii<h and 0<=jj<W:r[ii][jj]=k if v else oc
    return r
