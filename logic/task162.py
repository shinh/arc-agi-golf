def p(g,R=range(18)):# fill zero 3x3 w1s
 for i in R:
  t=g[i:i+3]
  for j in R:
   if sum(sum(r[j:j+3])for r in t)<1:
    for r in t:r[j:j+3]=[1]*3
 return g
