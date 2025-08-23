def p(g):
    # copy scaled pattern inside the frame defined by 4s
    R=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==4]
    if len(R)^4:return g
    (a,c),(b,d)=min(R),max(R)
    X=[0]*10;I=[(i,j,v)for i in range(a+1,b)for j in range(c+1,d)if(v:=g[i][j])if X.__setitem__(v,X[v]+1)or 1]
    Y=[0]*10;O=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if i<a or i>b or j<c or j>d if v if Y.__setitem__(v,Y[v]+1)or 1]
    r=max(x//y for x,y in zip(X,Y)if x*y)
    x,y=zip(*((i,j)for i,j,v in I if X[v]//Y[v]==r));e,f,k,l=min(x),max(x),min(y),max(y);x,y=zip(*((i,j)for i,j,v in O if X[v]//Y[v]==r));m,n,o,p=min(x),max(x),min(y),max(y)
    H=-~(l-k)//-~(p-o);V=-~(f-e)//-~(n-m)
    for i,j,v in[(V*(i-m)+x+e,H*(j-o)+y+k,v)for i,j,v in O for x in range(V)for y in range(H)]:g[i][j]=v
    return[r[c:d+1]for r in g[a:b+1]]
