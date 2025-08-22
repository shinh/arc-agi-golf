# copy motif into rectangular holes and extend rays

def p(g):
    bg=g[0][0]
    # Find the color of the center of the motif.
    for y,r in enumerate(g):
        for x,(c,nc,pc)in enumerate(zip(r,r[1:],[0]+r)):
            if bg!=c!=nc==pc!=bg and r.count(pc)>4:bc,mc=pc,c
    # Find the center of the motif.
    for y,r in enumerate(g):
        for x,(c,nc,pc)in enumerate(zip(r,r[1:],[0]+r)):
            if c==mc!=nc==pc!=bc:my,mx=y,x
    # Copy the motif and extend rays.
    h=len(g);w=len(r);R=range(-2,3);o=[r*1for r in g]
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c==mc and r[x-1]==bc:
                for dy in R:
                    for dx in R:
                        if g[my+dy][mx+dx]!=bg and 0<=y+dy<h and 0<=x+dx<w and g[y+dy][x+dx]==bc:o[y+dy][x+dx]=g[my+dy][mx+dx]
                for dy,dx in(0,1),(1,0),(-1,0),(0,-1):
                    rc=o[y+dy][x+dx]
                    if rc==o[y+dy*2][x+dx*2]:
                        ry,rx=y+dy*3,x+dx*3
                        while 0<=ry<h and 0<=rx<w and g[ry][rx]==bc:o[ry][rx]=rc;ry+=dy;rx+=dx
    # Remove the motif
    for dy in R:
        for dx in R:o[my+dy][mx+dx]=bg
    return o
