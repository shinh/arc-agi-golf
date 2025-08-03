def p(g):
    h=len(g);w=len(g[0]);o=[r[:] for r in g]
    for y in range(h):
        for x in range(w):
            if g[y][x]==2:
                if x+1<w and g[y][x+1]==2:
                    R0=max(0,y-1);R1=min(h-1,y+1);C0=max(0,x-1);C1=min(w-1,x+2)
                    for r in range(R0,R1+1):
                        for c in range(C0,C1+1):
                            if r in(R0,R1) or c in(C0,C1):
                                if o[r][c]!=2:o[r][c]=3
                if y+1<h and g[y+1][x]==2:
                    R0=max(0,y-1);R1=min(h-1,y+2);C0=max(0,x-1);C1=min(w-1,x+1)
                    for r in range(R0,R1+1):
                        for c in range(C0,C1+1):
                            if r in(R0,R1) or c in(C0,C1):
                                if o[r][c]!=2:o[r][c]=3
    return o

