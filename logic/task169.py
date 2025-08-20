def p(g):
    m={4:1,3:2,2:3}
    for y in range(10):
        for x in range(10):
            if g[y][x]==5:
                q=[(y,x)];g[y][x]=0;p=[]
                for i,j in q:
                    p+=(i,j),
                    for a,b in (1,0),(-1,0),(0,1),(0,-1):
                        A=i+a;B=j+b
                        if 0<=A<10 and 0<=B<10 and g[A][B]==5:
                            g[A][B]=0;q+=(A,B),
                c=m[len(p)]
                for i,j in p:g[i][j]=c
    return g
