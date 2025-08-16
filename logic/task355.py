def p(g):# rare color's neighborhood majority color
    h=len(g);w=len(g[0]);f=sum(g,[]);p=min(f,key=f.count);r=range
    u=[max(m:=[v for R in g[max(0,y-4):y+5] for v in R[max(0,x-4):x+5] if v-p],key=m.count)for y in r(h)
        for x in r(w)if p==g[y][x]]
    return[[max(u,key=u.count)]]
