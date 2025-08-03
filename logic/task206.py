def p(g):
    a=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v and v-5]
    y=min(y for y,x in a);x=min(x for y,x in a)
    s=[r[x:x+3]for r in g[y:y+3]]
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v==5:
                y-=1;x-=1
                for i in range(3):g[y+i][x:x+3]=s[i]
                return g
