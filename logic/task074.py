def p(g):
    t=((lambda i,j:(j,i),0,0),(lambda i,j:(29-i,29-j),2,2),(lambda i,j:(29-i,j),2,0),(lambda i,j:(i,29-j),0,2))
    for f,a,b in t:
        c=[(i,j,g[i][j]) for i in range(30) for j in range(30) if g[i][j]!=9]
        for i,j,v in c:
            x,y=f(i,j);x+=a;y+=b
            if x<30 and y<30:g[x][y]=v
    return g
