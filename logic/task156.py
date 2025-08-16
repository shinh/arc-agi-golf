def p(g):
    # bfs rectangles; fill interiors
    v=set();r=[];R=range(10)
    for y in R:
        for x in R:
            if(y,x)in v:continue
            t=g[y][x];q=[(y,x)];v|={(y,x)};a=b=y;c=d=x
            for i,j in q:
                a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
                for ny,nx in((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0<=ny<10>nx>=0 and g[ny][nx]==t and(ny,nx)not in v:v|={(ny,nx)};q+=[(ny,nx)]
            l=len(q);r+=[(l,a,b,c,d)]*(l==(b-a+1)*(d-c+1))
    if r:
        for(a,b,c,d),k in((min(r)[1:],1),(max(r)[1:],2)):
            for y in range(a+1,b):g[y][c+1:d]=[k]*(d-c-1)
    return g
