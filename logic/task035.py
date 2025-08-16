def p(g,E=enumerate):
    # replace 8 with closest color along cross
    o=[*map(list,g)]
    for y,r in E(g):
        for x,v in E(r):
            if v==8:
                for t in g[y+1:],g[:y][::-1]:
                    for w in t:
                        v=w[x]
                        if v:o[y][x]=v-8 and v or o[y][x];break
                for t in r[x+1:],r[:x][::-1]:
                    for v in t:
                        if v:o[y][x]=v-8 and v or o[y][x];break
    return o
