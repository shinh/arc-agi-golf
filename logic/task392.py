def p(g):# expand a found horizontal pattern
    for y in range(6):
        for x in range(6):
            if g[y][x]<1and(c:=g[y+1][x])*g[y][x+1]and(c in g[y][x+2:]):
                l=g[y][x+2:].index(c)
                return [[c+(5-c)*(max(i-y,1-l-i+y,j-x,1-l-j+x)%(-~l)!=1)for j in range(10)]for i in range(10)]
    return [*zip(*p([*zip(*g[::-1])]))][::-1]
