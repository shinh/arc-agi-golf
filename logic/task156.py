def p(g):
    # bfs rectangles; fill interiors
    v=set();r=[];R=range(10)
    for y in R:
        for x in R:
            if(y,x)in v:continue
            t=g[y][x];q=[(y,x)];v|={(y,x)};a=b=y;c=d=x;n=0
            for i,j in q:
                n+=1;a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ny,nx=i+dy,j+dx
                    if 0<=ny<10>nx>=0 and g[ny][nx]==t and(ny,nx)not in v:v|={(ny,nx)};q+=[(ny,nx)]
            if n==(b-a+1)*(d-c+1):r+=[(n,a,b,c,d)]
    if r:
        for(a,b,c,d),k in((min(r)[1:],1),(max(r)[1:],2)):
            for y in range(a+1,b):g[y][c+1:d]=[k]*(d-c-1)
    return g
