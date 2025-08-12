# 91 vs 77 (sota)
def p(g):
 n=sum(g,[]).count(5)
 return [[c*(c%5>0)for c in r[n:]+r[:n]]for r in g[-n:]+g[:-n]]
