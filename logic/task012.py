def p(g):
    o=create(12,12)
    for y in range(2,10):
        for x in range(2,10):
            c=g[y][x];a=g[y-1][x]
            if c and a==g[y+1][x]==g[y][x-1]==g[y][x+1]!=c:
                for j in range(-2,3):
                    for i in range(-2,3):
                        t,u=abs(i),abs(j)
                        if i==j==0 or t==u>0:o[y+j][x+i]=c
                        elif i*j==0:o[y+j][x+i]=a
    return o
