def p(g):
# stack nonzero cells up
 h=len(g)
 return[list(r)for r in zip(*[((*filter(None,c),)+(0,)*h)[:h]for c in zip(*g)])]
