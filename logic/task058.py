def p(g):# spiral of 3s
    x=y=j=0;i=1;l=m=len(g)-1;g[y][x]=3
    while l>0:
        for s in l,m:
            for _ in[0]*s:g[y:=y+j][x:=x+i]=3
            i,j=-j,i
        l=m;m-=2
    return g
