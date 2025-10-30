def p(g):
 t=[*zip(*g)];h=0
 for j,c in enumerate(t):
  if all(c):
   for R,a in zip(h:=h or[[0]*len(t)for _ in g],g):R[j]=R[j-(c[0]in a[:j])+(c[0]in a[j+1:])]=c[0]
 return h or[*zip(*p(t))]