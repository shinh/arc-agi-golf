def p(g):
    #slice+flip
    s=-~len(g)//(sum(2>len({*r})for r in g)+1)
    return[r[::s][::-1]for r in g[::s]]
