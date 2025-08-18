def p(g):
 # merge blocks separated by empty rows/cols, keep first colors
 a=sum;R=[];k=m=0
 for r in g:R+=k,;k+=a(r)<1;m=k+1 if a(r)else m
 C=[];k=n=0
 for c in zip(*g):C+=k,;k+=a(c)<1;n=k+1 if a(c)else n
 o=[[0]*n for _ in[0]*m]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v and not o[R[i]][C[j]]:o[R[i]][C[j]]=v
 return o

