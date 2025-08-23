#5shift
def p(g):
 n=str(g).count('5');return [[c%5and c for c in r[n:]+r[:n]]for r in g[-n:]+g[:-n]]
