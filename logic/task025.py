def p(g):
 t=[*zip(*g)];h=0
 for j,c in enumerate(t):
  if 0<min(c)==max(c):
   k=c[0];h=h or [[0]*len(t)for _ in g]
   for R,a in zip(h,g):R[j]=R[j-(k in a[:j])+(k in a[j+1:])]=k
 return h or [*zip(*p(t))]
