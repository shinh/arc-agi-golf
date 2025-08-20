# 385
# rotate to find bounding box then scale pattern into empty quadrants
def p(g):
    sx=sy=99
    ex=ey=-1
    q=g;R=range
    for o in R(80):
        q=[[[c,1][c>0and p&1]for c,p in zip(r,(0,*r))]for r in zip(*q[::-1])]

    for y in R(len(g)):
        for x in R(len(g[0])):
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
    for r in 3,2,1:
        for y in R(-7,len(g)-ly*r+1):
            for x in R(-7,len(g[0])-lx*r+1):
                if not((sy<=y<ey and sx<=x<ex)|(x>1and g[y][x-1])|(y>1and g[y-1][x]))and all(((y+dy>-1<x+dx)and g[y+dy][x+dx])==[0,0,2][g[sy+dy//r][sx+dx//r]]for dy in R(ly*r)for dx in R(lx*r)):
                    #print(f"OK {r=} {y=} {x=} {sy=} {sx=}")
                    for dy in R(ly*r):
                        for dx in R(lx*r):
                            if y+dy>-1<x+dx:
                                g[y+dy][x+dx]=g[sy+dy//r][sx+dx//r]
    return g
