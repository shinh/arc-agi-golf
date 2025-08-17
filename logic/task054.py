# copy motif into rectangular holes and extend rays

def p(g):
    bg=g[0][0]
    # Find the color of the center of the motif.
    for y,r in enumerate(g):
        for x,(c,nc,pc)in enumerate(zip(r,r[1:],[0]+r)):
            if bg!=c!=nc==pc!=bg:
                if r.count(pc)>4:bc,mc=pc,c

    # Find the center of the motif.
    for y,r in enumerate(g):
        for x,(c,nc,pc)in enumerate(zip(r,r[1:],[0]+r)):
            if c==mc!=nc==pc!=bc:
                my,mx=y,x
                #print(r,c,nc,pc)

    #show(g, "input")
    #print(f"{bg=} {mc=} {bc=} {my=} {mx=} {g[my][mx]=}")

    # Copy the motif and extend rays.
    o=[r*1for r in g]
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x]==mc and g[y][x-1]==bc:
                for dy in range(-2,3):
                    for dx in range(-2,3):
                        if g[my+dy][mx+dx]!=bg and 0<=y+dy<len(g) and 0<=x+dx<len(g[0])and g[y+dy][x+dx]==bc:
                            o[y+dy][x+dx]=g[my+dy][mx+dx]
                #show(o, "copy")

                for dy,dx in(0,1),(1,0),(-1,0),(0,-1):
                    rc=o[y+dy][x+dx]
                    if rc==o[y+dy*2][x+dx*2]:
                        ry,rx=y+dy*3,x+dx*3
                        while 0<=ry<len(g) and 0<=rx<len(g[0]) and g[ry][rx]==bc:
                            o[ry][rx]=rc
                            ry+=dy
                            rx+=dx
                #show(o, "ray")

    # Remove the motif
    for dy in range(-2,3):
        for dx in range(-2,3):
            o[my+dy][mx+dx]=bg
    #show(o, "output")

    return o
