def p(g):
    # keep cells touching b both axes
    f=sum(g,[]);b=max(range(1,10),key=f.count)
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v and v-b:
                r[x]=b*((y and g[y-1][x]==b or y<len(g)-1 and g[y+1][x]==b)*(x and r[x-1]==b or x<len(r)-1 and r[x+1]==b))
    return g
