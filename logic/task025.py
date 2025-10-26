def p(g):
 t=[*zip(*g)];h=[[0]*len(a)for a in g];f=0
 for j,c in enumerate(t):
  if 0<min(c)==max(c):
   f=1;k=c[0]
   for R,a in zip(h,g):R[j]=R[j-(k in a[:j])+(k in a[j+1:])]=k
 return f and h or [*zip(*p(t))]