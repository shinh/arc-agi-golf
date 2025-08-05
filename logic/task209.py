def p(g):
    h=len(g);w=len(g[0]);R=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==4]
    if len(R)-4:return g
    x,y=zip(*R);a=min(x);b=max(x);c=min(y);d=max(y)
    di={};I=[(i,j)for i in range(a+1,b)for j in range(c+1,d)if(v:=g[i][j])and(di.update({v:di.get(v,0)+1})or 1)]
    do={};O=[(i,j)for i in range(h)for j in range(w)if(i<a or i>b or j<c or j>d)and(v:=g[i][j])and(do.update({v:do.get(v,0)+1})or 1)]
    if not(I and O):return[r[c:d+1]for r in g[a:b+1]]
    x,y=zip(*O);A=min(x);B=max(x);C=min(y);D=max(y)
    t=[di[c]//do[c]for c in di if c in do];mc=max(set(t),key=t.count);sel={c for c in di if c in do and di[c]//do[c]==mc}
    x,y=zip(*[(i,j)for i,j in I if g[i][j]in sel]);e=min(x);f=max(x);k=min(y);l=max(y)
    x,y=zip(*[(i,j)for i,j in O if g[i][j]in sel]);m=min(x);n=max(x);o=min(y);p=max(y)
    H=(l-k+1)//(p-o+1);V=(f-e+1)//(n-m+1)
    S=[(V*(i-A)+x,H*(j-C)+y,v)for i in range(A,B+1)for j in range(C,D+1)if(v:=g[i][j])for x in range(V)for y in range(H)]
    sh=e-min(i for i,j,v in S if v in sel);sk=k-min(j for i,j,v in S if v in sel)
    for i,j,v in S:0<=i+sh<h and 0<=j+sk<w and g[i+sh].__setitem__(j+sk,v)
    return[r[c:d+1]for r in g[a:b+1]]
