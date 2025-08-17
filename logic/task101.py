# 396
def p(g):
    sx=sy=99
    ex=ey=-1
    q=g
    for o in range(80):
        q=[[[c,1][c>0and p&1]for c,p in zip(r,(0,*r))]for r in zip(*q[::-1])]

    for y in range(len(g)):
        for x in range(len(g[0])):
            if q[y][x]&1:
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
                if not((sy<=y<ey and sx<=x<ex)|(x>1and g[y][x-1])|(y>1and g[y-1][x]))and all([g[y+dy][x+dx],0][(y+dy<0)|(x+dx<0)]==[0,0,2][g[sy+dy//r][sx+dx//r]]for dy in range(ly*r)for dx in range(lx*r)):
                    #print(f"OK {r=} {y=} {x=} {sy=} {sx=}")
                    for dy in range(ly*r):
                        for dx in range(lx*r):
                            if y+dy>=0 and x+dx>=0:
                                g[y+dy][x+dx]=g[sy+dy//r][sx+dx//r]
    return g
