from collections import Counter as C
def p(g):
    h=16;w=12
    v=set();o=[]
    for y in range(h):
        for x in range(w):
            if g[y][x]==0 or(y,x)in v:continue
            q=[(y,x)];v.add((y,x));c=[]
            while q:
                i,j=q.pop();c.append((i,j,g[i][j]))
                for di in(-1,0,1):
                    for dj in(-1,0,1):
                        if di|dj:
                            ni,nj=i+di,j+dj
                            if 0<=ni<h and 0<=nj<w and g[ni][nj]and(ni,nj)not in v:
                                v.add((ni,nj));q.append((ni,nj))
            o.append(c)
    c=C();[c.update({v:1 for _,_,v in x})for x in o]
    k=max(c,key=c.get)
    s=[sum(v==k for _,_,v in x)for x in o]
    t=max([x for x,r in zip(o,s)if r==min(s)],key=len)
    o=[x for x in o if x is not t]
    ti=min(i for i,_,_ in t);tj=min(j for _,j,_ in t)
    t=[(i-ti,j-tj,v)for i,j,v in t]
    ci=min(i for i,j,v in t if v==k);cj=min(j for i,j,v in t if v==k)
    r=[row[:]for row in g]
    for x in o:
        xs=[(i,j)for i,j,v in x if v==k]
        mi=min(i for i,j in xs);mj=min(j for i,j in xs);w1=max(j for i,j in xs)-mj+1
        oc=next(v for _,_,v in x if v!=k)
        for i,j,v in t:
            for di in range(w1):
                for dj in range(w1):
                    ii=i*w1+di+mi-ci*w1;jj=j*w1+dj+mj-cj*w1
                    if 0<=ii<h and 0<=jj<w:r[ii][jj]=v if v==k else oc
    return r
