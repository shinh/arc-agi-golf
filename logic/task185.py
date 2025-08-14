def p(g):
    c=max(g[0])
    for i in range(2):
        g=[[*r]for r in zip(*g)if{*r}-{0,c}]
    return[[[0,g[y][x]][g[y][x]==g[y+1][x]==g[y][x+1]==g[y+1][x+1]!=c]for x in range(3)]for y in range(3)]
