def p(G):
    r=[r[:]for r in G];h=len(r);w=len(r[0]);g=sum(r,[]);C=g[:];d=[0]*10;o=[]
    for z,v in enumerate(g):
        if v<1:continue
        q=[z];g[z]=0
        for z in q:
            i,j=divmod(z,w)
            for I in range(i-1,i+2):
                for J in range(j-1,j+2):
                    n=I*w+J
                    if h>I>=0<=J<w and g[n]:g[n]=0;q+=n,
        for a in{C[u]for u in q}:d[a]+=1
        o+=q,
    k=d.index(max(d));t=min(o,key=lambda e:(sum(C[u]==k for u in e),-len(e)));o.remove(t)
    t=[divmod(z,w)for z in t];Y=min(i for i,_ in t);X=min(j for _,j in t)
    t=[(i-Y,j-X,r[i][j]==k)for i,j in t];y,x=min((i,j)for i,j,v in t if v)
    for e in o:
        m=[divmod(z,w)for z in e if C[z]==k];Y=min(i for i,_ in m);X=min(j for _,j in m);n=max(j for _,j in m)+1-X
        c=next(C[z]for z in e if C[z]!=k)
        for i,j,v in t:
            for a in range(n*n):
                ii=i*n+a//n+Y-y*n;jj=j*n+a%n+X-x*n
                if h>ii>=0<=jj<w:r[ii][jj]=[c,k][v]
    return r
