def p(g):
 g=[g,[*map(list,zip(*g))]][t:=max(g[0]+g[-1])<1];(s,c),(u,d)=sorted((r.index(v),v)for r in g for v in r if v)
 for r in g:r[s::u-s]=([c,d]*7)[:len(r[s::u-s])]
 return(g,[*zip(*g)])[t]
