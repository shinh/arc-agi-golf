def p(g):
 # combine quadrants
 n=min(len(g),len(g[0]));p=[r[:n]for r in g[:n]];g=[r[-n:]for r in g[-n:]]
 if'8'in str(p):p,g=g,p
 return[[a[x//n]*b[x%n]//8 for x in range(n*n)]for a in p for b in g]
