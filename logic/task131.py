def p(g):
 m=len(g[0]);n=len(g)
 if m>n:return[*zip(*p([*zip(*g)]))]
 i=([2in r for r in g]).index(1);return p(g[::-1])[::-1]if'3'in str(g[:i])else(g[:i+1]+[r for r in g if 3in r]+[m*[8]]+n*[m*[0]])[:n]
