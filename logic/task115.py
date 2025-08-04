def p(g):
    f=lambda a:list(dict.fromkeys(a))
    r=g[0]
    return [f(r)] if len(set(r))>1 else [[v]for v in f([row[0]for row in g])]
