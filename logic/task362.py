#5shift
def p(g):
 n=str(g).count('5');return [[c*(c!=5)for c in r[n:]+r[:n]]for r in g[-n:]+g[:-n]]
