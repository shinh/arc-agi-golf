def p(g):
    # find 2x2 color, rotate-crop, downscale
    c=[a for r,s in zip(g,g[1:]) for a,b,d,e in zip(r,r[1:],s,s[1:]) if a==b==d==e>0][-1]
    ac=sum({*sum(g,[])}-{c})
    for _ in[0]*96:g=[*zip(*g[-2+(c in g[-1])::-1])]
    r=len(g)//3
    return[[ac*(v==c)for v in row[::r]]for row in g[::r]]
