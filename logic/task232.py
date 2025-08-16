def p(g):
 # alt from first color with 5
 for R in g:
  for i,C in enumerate(R):
   if C>0:R[i:]=([C,5]*20)[:len(R)-i];break
 return g
