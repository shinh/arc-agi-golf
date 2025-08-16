def p(g):
    # flood-fill 0 rectangles
    h=len(g);w=len(g[0]);f=sum(g,[]);t=min(f,key=f.count)
    for i in range(h):
        for j in range(w):
            if g[i][j]:continue
            q=[(i,j)];g[i][j]=1
            for x,y in q:
                for X,Y in((1,0),(-1,0),(0,1),(0,-1)):
                    X+=x;Y+=y
                    if 0<=X<h and 0<=Y<w and g[X][Y]<1:g[X][Y]=1;q+=[(X,Y)]
            xs,ys=zip(*q);a,b=min(xs),min(ys);A,B=max(xs),max(ys)
            k=len(q)==(A-a+1)*(B-b+1)and all(g[x][y]-t if 0<=x<h and 0<=y<w else 1 for x,y in((a-2,b-1),(a-1,b-2),(a-2,B+1),(a-1,B+2),(A+2,b-1),(A+1,b-2),(A+2,B+1),(A+1,B+2)))and 4
            for x,y in q:g[x][y]=k
    return g
