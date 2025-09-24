def p(g):
    # flood-fill 0 rectangles
    h=len(g);w=len(g[0])
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v:continue
            q=[(i,j)];r[j]=1
            for x,y in q:
                for X,Y in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if-1<X<h and-1<Y<w and g[X][Y]<1:g[X][Y]=1;q+=[(X,Y)]
            x,y=zip(*q);a,A=min(x),max(x);b,B=min(y),max(y)
            k=len(q)==(A-a+1)*(B-b+1)and all(g[x][y]-5 for x,y in zip((a-2,a-1)*2+(A+2,A+1)*2,(b-1,b-2,B+1,B+2)*2)if-1<x<h and-1<y<w)and 4
            for x,y in q:g[x][y]=k
    return g
