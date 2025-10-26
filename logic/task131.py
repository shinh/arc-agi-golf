def p(g):
 n=len(g);m=len(g[0])
 if m>n:return[*zip(*p([*zip(*g)]))]
 i=([2 in r for r in g]).index(1)
 return p(g[::-1])[::-1]if any(3 in r for r in g[:i])else(g[:i+1]+[r for r in g if 3 in r]+[[8]*m]+[[0]*m]*n)[:n]