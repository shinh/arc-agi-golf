def p(g):
 C=sum(g,[]);A=next(filter(None,C[::-1]));D=min({*C}-{0,A})
 for E,B in enumerate(zip(*g)):
  if D in B and A in B[(G:=19-B[::-1].index(D))+1:]:
   for R in g[G:]:R[E]=R[E]or A
 return g