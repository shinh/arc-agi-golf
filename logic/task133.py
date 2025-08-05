def p(G):
    r=[r[:]for r in G];h=len(r);w=len(r[0]);g=sum(r,[]);d=[0]*10;o=[];s=set()
    for z in range(len(g)):
        if g[z]<1 or z in s:continue
        q=[z];s|={z};c=[z]
        for z in q:
            i,j=divmod(z,w)
            for I in range(i-1,i+2):
                for J in range(j-1,j+2):
                    n=I*w+J
                    if 0<=I<h and 0<=J<w and g[n]and n not in s:
                        s|={n};q+=n,;c+=n,
        for a in{g[u]for u in c}:d[a]+=1
        o+=c,
    k=d.index(max(d));t=min(o,key=lambda e:(sum(g[u]==k for u in e),-len(e)));o.remove(t)
    t=[divmod(z,w)for z in t];ti=min(i for i,_ in t);tj=min(j for _,j in t)
    t=[(i-ti,j-tj,r[i][j]==k)for i,j in t];y,x=min((i,j)for i,j,v in t if v)
    for e in o:
        m=[divmod(z,w)for z in e if g[z]==k];ys,xs=zip(*m);Y=min(ys);X=min(xs);n=max(xs)+1-X
        oc=next(g[z]for z in e if g[z]!=k)
        for i,j,v in t:
            for a in range(n*n):
                ii=i*n+a//n+Y-y*n;jj=j*n+a%n+X-x*n
                if 0<=ii<h and 0<=jj<w:r[ii][jj]=[oc,k][v]
    return r
