def p(g):
    # grow 3s over 1s with >=2 big neighbors
    for n in range(289):
        if (r:=g[y:=n//17])[x:=n%17]==1<sum((y and g[y-1][x]>2,y<16 and g[y+1][x]>2,x and r[x-1]>2,x<16 and r[x+1]>2)):
            r[x]=3
            return p(g)
    return g
