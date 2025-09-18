def p(g):# spiral3
    x=y=j=0;i=1;n=len(g)-1
    for k in range(n*2+1):
        for _ in[0]+[1]*(n-((k-(k>1))&-2)):g[y:=y+j*_][x:=x+i*_]=3
        i,j=-j,i
    return g
