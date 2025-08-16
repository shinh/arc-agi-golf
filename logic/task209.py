def p(g):
    # copy scaled pattern inside the frame defined by 4s
    h=len(g);w=len(g[0]);R=[(i,j)for i in range(h)for j in range(w)if g[i][j]==4]
    if len(R)^4:return g
    (a,c),(b,d)=min(R),max(R)
    X=[0]*10;I=[(i,j,v)for i in range(a+1,b)for j in range(c+1,d)if(v:=g[i][j])if X.__setitem__(v,X[v]+1)or 1]
    Y=[0]*10;O=[(i,j,v)for i in range(h)for j in range(w)if i<a or i>b or j<c or j>d if(v:=g[i][j])if Y.__setitem__(v,Y[v]+1)or 1]
    r=max(X[i]//Y[i]for i in range(10)if X[i]and Y[i])
    x,y,_=zip(*O);A=min(x);C=min(y);x,y=zip(*((i,j)for i,j,v in I if X[v]//Y[v]==r));e,f,k,l=min(x),max(x),min(y),max(y);x,y=zip(*((i,j)for i,j,v in O if X[v]//Y[v]==r));m,n,o,p=min(x),max(x),min(y),max(y)
    H=-~(l-k)//-~(p-o);V=-~(f-e)//-~(n-m);sh=e-V*(m-A);sk=k-H*(o-C)
    for i,j,v in[(V*(i-A)+x+sh,H*(j-C)+y+sk,v)for i,j,v in O for x in range(V)for y in range(H)]:0<=i<h and 0<=j<w and g[i].__setitem__(j,v)
    return[r[c:d+1]for r in g[a:b+1]]
