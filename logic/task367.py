def p(g):
    # flood-fill 0 rectangles
    h=len(g);w=len(g[0])
    for i in range(h):
        for j in range(w):
            if g[i][j]:continue
            q=[(i,j)];g[i][j]=1
            for x,y in q:
                for X,Y in((1,0),(-1,0),(0,1),(0,-1)):
                    X+=x;Y+=y
                    if -1<X<h and -1<Y<w and g[X][Y]<1:g[X][Y]=1;q+=[(X,Y)]
            x,y=zip(*q);a,A=min(x),max(x);b,B=min(y),max(y)
            k=len(q)==(A-a+1)*(B-b+1)and 5 not in[g[x][y]for x,y in zip((a-2,a-1)*2+(A+2,A+1)*2,(b-1,b-2,B+1,B+2)*2)if -1<x<h and-1<y<w]and 4
            for x,y in q:g[x][y]=k
    return g
