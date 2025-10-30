def p(g):
 C=sum(g,[])
 while(A:=C.pop())<1:0
 D,={*C}-{0,A}
 for E,B in enumerate(zip(*g)):
  if D in B and A in B[(G:=B.index(D)):]:
   for R in g[G:]:R[E]=R[E]or A
 return g
