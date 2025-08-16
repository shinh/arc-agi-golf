def p(g):
    # find 2x2 color, rotate-crop, downscale
    for r,pr in zip(g,g[1:]):
        for x in range(len(r)-1):
            if (v:=r[x])==pr[x]==r[x+1]==pr[x+1]!=0:c=v
    ac=({*sum(g,[])}-{0,c}).pop()
    for _ in[0]*96:g=[*zip(*g[-2+(c in g[-1])::-1])]
    r=len(g)//3
    return[[ac*(g[y*r][x*r]==c)for x in range(3)]for y in range(3)]
