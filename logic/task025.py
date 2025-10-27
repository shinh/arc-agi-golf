# fuse
def p(g):
 t=[*zip(*g)];h=0
 for j,c in enumerate(t):
  if(k:=min(c))==max(c)>0:
   for R,a in zip(h:=h or[[0]*len(t)for _ in g],g):R[j]=R[j-(k in a[:j])+(k in a[j+1:])]=k
 return h or[*zip(*p(t))]
