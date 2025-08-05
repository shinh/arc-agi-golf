def p(g):
    f=lambda a:list(dict.fromkeys(a))
    r=g[0]
    return[[[v]for v in f([row[0]for row in g])],[f(r)]][len(set(r))>1]
