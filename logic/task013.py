def p(g):
 g=[g,[*map(list,zip(*g))]][t:=1>max(g[0]+g[-1])];s,c=min(a:=[(j,v)for r in g for j,v in enumerate(r)if v]);u,d=max(a)
 for r in g:r[s::u-s]=((c,d)*7)[:len(r[s::u-s])]
 return[g,[*zip(*g)]][t]
