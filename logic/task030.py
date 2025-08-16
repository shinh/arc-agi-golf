def p(g):
 # align colors to first row of 1
 f=sum(g,[]);i=f.index;w=len(g[0]);u=i(1)//w;o=[[0]*w for _ in g]
 for k,c in enumerate(f):
  if c:o[k//w+u-i(c)//w][k%w]=c
 return o
