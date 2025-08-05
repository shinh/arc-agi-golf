def p(g):
    h=len(g);w=len(g[0]);R=[(i,j)for i in range(h)for j in range(w)if g[i][j]==4]
    if len(R)^4:return g
    (a,c),(b,d)=min(R),max(R)
    x=[0]*10;I=[(i,j,v)for i in range(a+1,b)for j in range(c+1,d)if(v:=g[i][j])if x.__setitem__(v,x[v]+1)or 1]
    y=[0]*10;O=[(i,j,v)for i in range(h)for j in range(w)if i<a or i>b or j<c or j>d if(v:=g[i][j])if y.__setitem__(v,y[v]+1)or 1]
    if not(I and O):return[r[c:d+1]for r in g[a:b+1]]
    t=[x[c]//y[c]for c in range(10)if x[c]and y[c]];mc=max({*t},key=t.count);sel=[c for c in range(10)if x[c]and y[c]and x[c]//y[c]==mc]
    x,y,_=zip(*O);A=min(x);B=max(x);C=min(y);D=max(y)
    x,y=zip(*((i,j)for i,j,v in I if v in sel));e=min(x);f=max(x);k=min(y);l=max(y)
    x,y=zip(*((i,j)for i,j,v in O if v in sel));m=min(x);n=max(x);o=min(y);p=max(y)
    H=-~(l-k)//-~(p-o);V=-~(f-e)//-~(n-m)
    sh=e-V*(m-A);sk=k-H*(o-C)
    for i,j,v in [(V*(i-A)+x,H*(j-C)+y,v)for i in range(A,B+1)for j in range(C,D+1)if(v:=g[i][j])for x in range(V)for y in range(H)]:0<=i+sh<h and 0<=j+sk<w and g[i+sh].__setitem__(j+sk,v)
    return[r[c:d+1]for r in g[a:b+1]]
