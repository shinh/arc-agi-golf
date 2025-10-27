# copy motif into rectangular holes and extend rays

def p(g):
    bg=g[0][0]
    # Find the color of the center of the motif.
    for y,r in enumerate(g):
        for x,(c,nc,pc)in enumerate(zip(r,r[1:],[bg]+r)):
            if bg!=c!=nc==pc!=bg and r.count(pc)>4:bc,mc=pc,c
    # Find the center of the motif.
    for y,r in enumerate(g):
        for x,(c,nc,pc)in enumerate(zip(r,r[1:],[bg]+r)):
            if c==mc!=nc==pc!=bc:u,v=y,x
    # Copy the motif and extend rays.
    h=len(g);w=len(g[0]);R=range(-2,3);o=[r[:]for r in g]
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c==mc and r[x-1]==bc:
                for dy in R:
                    for dx in R:
                        Y=y+dy;X=x+dx
                        if g[u+dy][v+dx]!=bg and h>Y>=0 and w>X>=0 and g[Y][X]==bc:o[Y][X]=g[u+dy][v+dx]
                for dy,dx in((0,1),(1,0),(-1,0),(0,-1)):
                    rc=o[y+dy][x+dx]
                    if rc==o[y+dy*2][x+dx*2]:
                        Y=y+dy*3;X=x+dx*3
                        while h>Y>=0 and w>X>=0 and g[Y][X]==bc:o[Y][X]=rc;Y+=dy;X+=dx
    # Remove the motif
    for dy in R:
        for dx in R:o[u+dy][v+dx]=bg
    return o
