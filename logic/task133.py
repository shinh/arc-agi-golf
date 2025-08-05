def p(G):
    r=[r[:]for r in G];h=len(r);w=len(r[0]);g=sum(r,[]);d=[0]*10;o=[]
    for z,v in enumerate(g):
        if v<1:continue
        q=[z];g[z]=-v
        for z in q:
            i,j=divmod(z,w)
            for I in i-1,i,i+1:
                for J in j-1,j,j+1:
                    if h>I>=0<=J<w and 0<g[n:=I*w+J]:g[n]=-g[n];q+=n,
        for a in{-g[u]for u in q}:d[a]+=1
        o+=q,
    k=d.index(max(d));t=min(o,key=lambda e:(sum(-g[u]==k for u in e),-len(e)));o.remove(t)
    t=[divmod(z,w)for z in t];Y,X=map(min,zip(*t))
    t=[(i-Y,j-X,r[i][j]==k)for i,j in t];y,x=min((i,j)for i,j,v in t if v)
    for e in o:
        m=[divmod(z,w)for z in e if -g[z]==k];Y,X=map(min,zip(*m));n=max(j for _,j in m)+1-X
        c=next(-g[z]for z in e if -g[z]!=k)
        for i,j,v in t:
            for a in range(n*n):r[i*n+a//n+Y-y*n][j*n+a%n+X-x*n]=[c,k][v]
    return r
