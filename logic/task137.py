def p(g):
    # expand rare color rectangle outward
    w=len(g[0]);a=sum(g,[]);c=min({*a},key=a.count)
    y,x=zip(*(divmod(i,w)for i,v in enumerate(a)if v==c))
    y=sorted(y);x=sorted(x);Y=y[1];X=x[1];s=Y-y[0]
    for k in range(len(g)*w):i,j=divmod(k,w);g[i][j]=[g[i][j],c][max(abs(i-Y),abs(j-X))%s<1]
    return g
