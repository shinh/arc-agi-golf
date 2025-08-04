def p(g):
    n=len(g)
    t=((lambda i,j:(j,i),0,0),(lambda i,j:(n-1-i,n-1-j),2,2),(lambda i,j:(n-1-i,j),2,0),(lambda i,j:(i,n-1-j),0,2))
    for f,a,b in t:
        c=[(i,j,g[i][j]) for i in range(n) for j in range(n) if g[i][j]!=9]
        for i,j,v in c:
            x,y=f(i,j);x+=a;y+=b
            if x<n and y<n:g[x][y]=v
    return g
