def p(g):
    # rotate to match shape then drop rare color
    s={18,9,15,3,11,21,27,16,19,10}
    for pc in range(10):
        P={(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==pc}
        if P:
            my,mx=map(min,zip(*P))
            if {(y-my)*7+x-mx for y,x in P}==s:break
    g=[*map(list,zip(*g))]
    for r in g:
        if pc in r:
            x=r.index(pc)
            while r[x]==pc:
                x+=1
            nc=set(r[x:])-{0}
            if nc:
                nc=nc.pop()
                r[x:]=[nc]*(len(r)-x)
    return[*map(list,zip(*g))]
