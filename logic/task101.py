def p(g):
    sx=sy=99
    ex=ey=-1
    q=g
    for o in range(80):
        q=[[[c,1][c>0and p==1]for c,p in zip(r,(0,*r))]for r in zip(*q[::-1])]

    for y in range(len(g)):
        for x in range(len(g[0])):
            if q[y][x]==1:
                sx=min(sx,x)
                sy=min(sy,y)
                ex=max(ex,x+1)
                ey=max(ey,y+1)
    #print(sx,sy,ex,ey)
    #show(g,"hm")

    lx=ex-sx
    ly=ey-sy

    #show(g,"hm")
    #print('start',f"{sx=} {sy=} {ex=} {ey=}")
    for r in range(3,0,-1):
        for y in range(-7,len(g)-ly*r+1):
            for x in range(-7,len(g[0])-lx*r+1):
                if sy<=y<ey and sx<=x<ex:continue
                if x>1and g[y][x-1]:continue
                if y>1and g[y-1][x]:continue
                ok=True
                for dy in range(ly*r):
                    for dx in range(lx*r):
                        if y+dy<0 or x+dx<0:d=0
                        else:d=g[y+dy][x+dx]
                        c=g[sy+dy//r][sx+dx//r]
                        #if y==7 and x==1:print("kk",dy,dx,d,c,ly,lx,r)
                        if d!=[0,0,2][c]:
                            ok=False
                if ok:
                    #print(f"OK {r=} {y=} {x=} {sy=} {sx=}")
                    for dy in range(ly*r):
                        for dx in range(lx*r):
                            if y+dy>=0 and x+dx>=0:
                                g[y+dy][x+dx]=g[sy+dy//r][sx+dx//r]
    return g
