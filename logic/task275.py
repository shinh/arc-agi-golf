def p(g):
 # combine quadrants
 n=min(len(g),len(g[0]));p,g=[r[:n]for r in g[:n]],[r[-n:]for r in g[-n:]]
 if'8'in str(p):p,g=g,p
 return[[x*y//8for x in a for y in b]for a in p for b in g]
