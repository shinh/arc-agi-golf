def p(g):
    # replace 8 with closest color along cross
    # scan column and row slices sequentially
    z=[*zip(*g)];o=[*map(list,g)]
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==8:
                for t in z[x][y+1:],z[x][:y][::-1],r[x+1:],r[:x][::-1]:
                    for v in t:
                        if v:o[y][x]=v-8 and v or o[y][x];break
    return o
