def p(g):
    h=w=12;o=[r for r in g];v=[[0]*w for _ in g]
    for y in range(h):
        for x in range(w):
            if g[y][x]==0 and not v[y][x]:
                q=[(y,x)];v[y][x]=1;S=[(y,x)]
                while q:
                    y1,x1=q.pop()
                    for y2,x2 in((y1-1,x1),(y1+1,x1),(y1,x1-1),(y1,x1+1)):
                        if 0<=y2<h and 0<=x2<w and g[y2][x2]==0 and not v[y2][x2]:
                            v[y2][x2]=1;q.append((y2,x2));S.append((y2,x2))
                ys=[s[0] for s in S];xs=[s[1] for s in S]
                a,b=min(ys),max(ys);c,d=min(xs),max(xs)
                if b-a==d-c and len(S)==(b-a+1)*(d-c+1) and all(g[a-1][i]==g[b+1][i]==5 for i in range(c,d+1)) and all(g[i][c-1]==g[i][d+1]==5 for i in range(a,b+1)):
                    for y1,x1 in S:o[y1][x1]=2
    return o
