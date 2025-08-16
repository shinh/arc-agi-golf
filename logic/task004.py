# Shift each color right except bottom and right edges.

def p(g):
 o=[[0]*len(r)for r in g];S={};i=len(g)
 while i:
  i-=1;j=len(g[i])
  while j:
   j-=1
   if(v:=g[i][j]):b,m=S.setdefault(v,(i,j));o[i][j+(i<b)*(j<m)]=v
 return o
