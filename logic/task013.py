def p(g):
 t=not any(g[0]+g[-1]);g=[*map(list,zip(*g))]*t or g
 a=[(j,v)for r in g for j,v in enumerate(r)if v];s,c=min(a);u,d=max(a)
 for r in g:r[s::u-s]=((c,d)*20)[:len(r[s::u-s])]
 return [*zip(*g)]*t or g