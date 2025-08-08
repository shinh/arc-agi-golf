def p(g):
    v=set();o=[r for r in g]
    for y in range(9):
        for x in range(9):
            if g[y][x]==0 or (y,x) in v:continue
            s=[(y,x)];obj=[]
            while s:
                y1,x1=s.pop()
                if (y1,x1) in v or g[y1][x1]==0:continue
                v.add((y1,x1));obj.append((y1,x1))
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ny,nx=y1+dy,x1+dx
                    if 0<=ny<9 and 0<=nx<9:s.append((ny,nx))
            c=[g[a][b] for a,b in obj if g[a][b]!=2][0]
            my=min(a for a,_ in obj);mx=min(b for _,b in obj)
            d=[(-1 if a==my else 1,-1 if b==mx else 1) for a,b in obj if g[a][b]==2]
            S=set()
            for dy,dx in d:
                for a,b in obj:
                    y2,x2=a,b
                    while 0<=y2<9 and 0<=x2<9:
                        S.add((y2,x2));y2+=dy;x2+=dx
            for a,b in S:o[a][b]=c
    return o

