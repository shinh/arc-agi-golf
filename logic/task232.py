def p(g):
 # alt from first color with 5
 for R in g:
  for i,C in enumerate(R):
   if C:R[i:]=([C,5]*7)[:len(R)-i];break
 return g
